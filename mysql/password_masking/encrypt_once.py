from cryptography.fernet import Fernet
from password_utils import encrypt_password


def generate_key():
    key=Fernet.generate_key()
    with open('secret.key','wb') as f:
        f.write(key)


if __name__ =='__main__':
    generate_key()

    encrypted=encrypt_password('Slim@3103')
    print('Copy the password to utils.py')
    print(encrypted)
