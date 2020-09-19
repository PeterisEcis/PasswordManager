import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import fernet

class Crypto:
    def __init__(self, password):
        self.key = self.GenerateKey(password)

    def GenerateKey(self, password):
        # change salt when using
        salt = b'\xcfz@\xf5\x9f\xcam\x8bu\x99=\x02\xd1Y\xa0\xa6'
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations=100000,
        backend = default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

    def EncryptString(self, message):
        encoded = message.encode()
        f = Fernet(self.key)
        encrypted - f.encrypt(encoded)
        return encrypted
    
    def DecryptString(self, encrypted):
        f = Fernet(self.key)
        decrypted = f.decrypt(encrypted)
        message = decrypted.decode()
        return message

    #TODO: Incorrect key error handling

