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
        #salt = b'_salt'
        salt = b'\x19H\xbc\x9fTg\x91\x1a\xf5\xda^|\t\x92\x18\xc4\xe2Ox\xfc\xa7 U4\x17\xf5\xe1\x977\x0bvB'
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
        try:
            decrypted = self.token.decrypt(encrypted.encode(self.encoding))
            return decrypted.decode(self.encoding)
        except:
            print("Wrong password!")
            return False

    #TODO: Incorrect key error handling

