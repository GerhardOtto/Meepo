import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import secrets
import base64

# def createKey():
#     myKey = Fernet.generateKey()
#     with open("key.key", "wb") as keyFile:
#         keyFile.write(key)


def loadKey():
    return open("key.key", "rb").read()


# load the previously generated key
key = loadKey()

def generateSalt(size=16):
    return secrets.token_bytes(size)


def deriveKey(salt, password):
    key = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return key.derive(password.encode())


# load salt from salt.salt file
def loadSalt():
    return open("salt.salt", "rb").read()


def generateKey(password, saltSize=16, oldSalt=False, saveSalt=True):
    if oldSalt:
        # load existing salt
        salt = loadSalt()
    elif saveSalt:
        # generate new salt and save it
        salt = generateSalt(saltSize)
        with open("salt.salt", "wb") as saltFile:
            saltFile.write(salt)
    # generate the key from the salt and the password
    derivedKey = deriveKey(salt, password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derivedKey)


def encrypt(filename, key):
    fernetKey = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encryptedData = fernetKey.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encryptedData)


def decrypt(filename, key):
    ernetKey = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encryptedData = file.read()
    # decrypt data
    try:
        decryptedData = ernetKey.decrypt(encryptedData)
    except cryptography.fernet.InvalidToken:
        print("Incorrect password")
        return
    # write the original file
    with open(filename, "wb") as file:
        file.write(decryptedData)
    print("Decrypted file successfully")