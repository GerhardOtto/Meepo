import hashlib

def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')
    hashObject = hashlib.sha256()
    hashObject.update(passwordBytes)
    hashedPassword = hashObject.hexdigest()
    print(hashedPassword)
    return hashedPassword



def rsaAlgoEncoder(binary, hashedPassword):
    binaryLen = len(binary)
    encodedText = ""
    for i in range(binaryLen):
        currentChar = binary[i]
        print(currentChar)
        cypherNum = (currentChar ** 5) % 14
        print(cypherNum)
        encodedText = cypherNum 
        # convert it to bytes
    encodedText = str(encodedText)
    encodedText = hashedPassword + encodedText
    
    return encodedText


def ownAlgoEncoder(data, hashedPassword):
    n = len(data)
    hashedPasswordBytes = bytearray(hashedPassword, "utf-8")
    encodedData = bytearray(n)
    for i in range(n):
        encodedData[i] = data[n - i - 1] ^ hashedPasswordBytes[i % len(hashedPasswordBytes)]
    
    return encodedData



def ownAlgoDecoder(encodedData, hashedPassword):
    n = len(encodedData)
    hashedPasswordBytes = bytearray(hashedPassword, "utf-8")
    decodedData = bytearray(n)
    for i in range(n):
        decodedData[i] = encodedData[n - i - 1] ^ hashedPasswordBytes[i % len(hashedPasswordBytes)]
    
    return decodedData


def rsaAlgoDecoder(encodedText, hashedPassword):
    decodedText = ""
    encodedLength = len(encodedText)
    for i in range(encodedLength):
        currentChar = encodedText[i]
        unicoceValue = ord(currentChar)
        cypherNum = (unicoceValue ** 11) % 14
        cypherChar = chr(cypherNum)
        #cypherChar = round(cypherChar)
        decodedText += cypherChar

    return decodedText
