from cryptography.fernet import Fernet

# Carregar a chave
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Descriptografar o arquivo testfile.txt
def decrypt_file(file_path):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"Arquivo '{file_path}' descriptografado com sucesso!")

# Descriptografar o arquivo de teste
decrypt_file("testfile.txt")
