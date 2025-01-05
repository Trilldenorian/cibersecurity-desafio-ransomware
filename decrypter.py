import os
import pyaes

# Função para descriptografar o arquivo
def decrypt_file(file_name, encryption_key):
    # Verifica se o arquivo criptografado existe
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado.")
    
    # Tamanho da chave de criptografia para AES deve ser 16, 24 ou 32 bytes
    if len(encryption_key) not in [16, 24, 32]:
        raise ValueError("A chave de criptografia deve ter 16, 24 ou 32 bytes.")
    
    # Lê o arquivo criptografado
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()

    # Descriptografa os dados usando AES em modo CTR
    aes = pyaes.AESModeOfOperationCTR(encryption_key)
    decrypted_data = aes.decrypt(encrypted_data)

    # Nome do arquivo descriptografado
    decrypted_file_name = f"{file_name.replace('.ransomwaretroll', '')}"

    # Cria o arquivo descriptografado
    with open(decrypted_file_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Arquivo descriptografado com sucesso: {decrypted_file_name}")
    
    # Após a descriptografia, podemos remover o arquivo criptografado, se necessário
    os.remove(file_name)
    print(f"Arquivo criptografado {file_name} removido.")

# Configurações iniciais
file_name = "teste.txt.ransomwaretroll"  # O arquivo criptografado
key = b"8A0j$Tax^Vp4x%UJn@X2@fV#"  # A chave de criptografia precisa ser de 16, 24 ou 32 bytes

try:
    decrypt_file(file_name, key)
except Exception as e:
    print(f"Erro durante a descriptografia: {e}")

