from cryptography.fernet import Fernet

# Gerar uma chave de criptografia
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Carregar a chave
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Criptografar o arquivo testfile.txt
def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        original_data = file.read()
    
    encrypted_data = fernet.encrypt(original_data)
    
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"Arquivo '{file_path}' criptografado com sucesso!")

# Criptografar o arquivo de teste
encrypt_file("testfile.txt")
