from cryptography.fernet import Fernet

def load_key():
    return open('Secret.key','rb').read()

class FakeStr(str):
    def __str__(self):
        return "*****"
    def __repr__(self):
        return "*****"


def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypt_password):
    key=load_key()
    f=Fernet(key)
    decrypted=f.decrypt(encrypt_password.decoed())
    return FakeStr(decrypted)


def get_decrypt_password():
    encrypt_password = b'gAAAAABpG5ndIzFKvi7vQNWBc8CNAcgyizFxfe2R7GB11VcPIq6YhPdfcAW1GJqYFPZDZ6ic3ndCtH2o4fwbhjnyP104pW_KOA==
    return decrypt_password(encrypt_password)