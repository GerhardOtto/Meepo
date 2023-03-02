import hashlib

def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')

    hashObject = hashlib.sha256()

    hashObject.update(passwordBytes)

    hashedPassword = hashObject.hexdigest()

    return hashedPassword


def ownAlgoEncoder(base64, hashedPassword):

    notBase64 = base64 + hashedPassword
    return notBase64