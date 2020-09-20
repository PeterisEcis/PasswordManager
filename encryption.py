import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

class Crypto:
    def __init__(self, password):
        self.encoding = 'utf-8'
        self.key = self.GenerateKey(password)
        self.token = Fernet(self.key)

    def GenerateKey(self, password):
        # change salt when using
        password = password.encode()
        salt = b'_salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length = 32,
            salt = salt,
            iterations=100000,
            backend = default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    
    def get_key(self, password):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password.encode(self.encoding))
        return base64.urlsafe_b64encode(digest.finalize())

    def EncryptString(self, message):
        encrypted = self.token.encrypt(message.encode(self.encoding))
        return encrypted.decode(self.encoding)
    
    def DecryptString(self, encrypted):
        decrypted = self.token.decrypt(encrypted.encode(self.encoding))
        return decrypted.decode(self.encoding)

    #TODO: Incorrect key error handling

