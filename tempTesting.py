from encryption import Crypto

if __name__ == "__main__":
    crypto = Crypto(input("Enter you password: "))
    encrypted = input("encrypted string: ")
    message = "secret message"
    print(str(crypto.token))
    #encrypted = crypto.EncryptString(message)
    print(encrypted)
    print(crypto.DecryptString(encrypted))