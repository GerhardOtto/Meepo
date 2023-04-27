import hashlib

def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')
    hashObject = hashlib.sha256()
    hashObject.update(passwordBytes)
    hashedPassword = hashObject.hexdigest()

    return hashedPassword


def ownAlgoEncoder(data, hashedPassword):
    n = len(data)
    hashedPasswordBytes = bytes(hashedPassword, "utf-8")
    encodedData = bytearray(n)
    for i in range(n):
        encodedData[i] = data[n - i - 1] ^ hashedPasswordBytes[i % len(hashedPasswordBytes)]
    
    return encodedData


def ownAlgoDecoder(encodedData, hashedPassword):
    n = len(encodedData)
    hashedPasswordBytes = bytes(hashedPassword, "utf-8")
    decodedData = bytearray(n)
    for i in range(n):
        decodedData[i] = encodedData[n - i - 1] ^ hashedPasswordBytes[i % len(hashedPasswordBytes)]
    
    return decodedData


