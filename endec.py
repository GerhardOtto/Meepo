import hashlib

def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')
    hashObject = hashlib.sha256()
    hashObject.update(passwordBytes)
    hashedPassword = hashObject.hexdigest()
    print(hashedPassword)
    return hashedPassword


def compareAndDecode(password,encodedText,decodedText):
    passwordLength = len(password)
    for i in range(passwordLength):
        if password[i] == encodedText[i]:
            decodedText = rsaAlgoDecoder(encodedText)
        else:
             decodedText = "Nice try!"

        return decodedText


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

def ownAlgoEncoder(binary, hashedPassword):

    n = len(binary)
    encodedText = ''
    for i in range(n):
        if i % 2 == 0:
            encodedText += input[n - i//2 - 1]
        else:
            encodedText += input[i//2]
    
    return encodedText


def ownAlgoDecoder(encodedText, hashedPassword):

    # remove hashedpassword
    # loop 3 tiems
    # save output

    return decodedText


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
