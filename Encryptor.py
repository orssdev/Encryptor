from cryptography.fernet import Fernet
import base64, hashlib, os

input_key = input('Enter Key: ')
raw_hash = hashlib.sha256(input_key.encode()).digest()
key = base64.urlsafe_b64encode(raw_hash)
cipher = Fernet(key)


def encrpyt_file(input_file, output_file):
    try:
        with open(os.path.join('decrypted_input', input_file), 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(os.path.join('encrypted_output', output_file), 'wb') as f:
            f.write(encrypted)
    except:
        print('Could Not Open', input_file)


def decrypt_file(input_file, output_file):
    try:
        with open(os.path.join('encrypted_input', input_file), 'rb') as f:
            data = f.read()
        decrypted = cipher.decrypt(data)
        with open(os.path.join('decrypted_output', output_file), 'wb') as f:
            f.write(decrypted)
    except:
        print('Could Not Open', input_file)

# input_file = input('Input file: ')
# encrpyt_file(input_file, f'{input_file}.enc')

input_file = input('Input file: ')
decrypt_file(input_file, os.path.splitext(input_file)[0])