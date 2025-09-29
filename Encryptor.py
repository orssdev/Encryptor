from cryptography.fernet import Fernet

key = Fernet.generate_key()
print('Key:', key.decode())

cipher = Fernet(key)

data = 'Hello World!'.encode()
encrpyted = cipher.encrypt(data)
print('Encrypted:', encrpyted)

decrypted = cipher.decrypt(encrpyted)
print('Decrypted', decrypted.decode())