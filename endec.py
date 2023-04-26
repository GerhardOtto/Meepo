import hashlib

def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')
    hashObject = hashlib.sha256()
    hashObject.update(passwordBytes)
    hashedPassword = hashObject.hexdigest()
    print(hashedPassword)
    return hashedPassword


# def compareAndDecode(password,encodedText,decodedText):
#     passwordLength = len(password)
#     for i in range(passwordLength):
#         if password[i] == encodedText[i]:
#             decodedText = rsaAlgoDecoder(encodedText)
#         else:
#              decodedText = "Nice try!"

#         return decodedText


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

# def ownAlgoEncoder(binaryFilePath, hashedPassword):
#     n = len(binaryFilePath)
#     encodedText = ''
#     for i in range(n):
#         if i % 2 == 0:
#             encodedText += input[n - i//2 - 1]
#         else:
#             encodedText += input[i//2]
    
#     return encodedText

def ownAlgoEncoder(data, hashed_password):
    n = len(data)
    hashed_password_bytes = bytearray(hashed_password, "utf-8")
    encoded_data = bytearray(n)
    for i in range(n):
        encoded_data[i] = data[n - i - 1] ^ hashed_password_bytes[i % len(hashed_password_bytes)]
    
    return encoded_data


# def ownAlgoDecoder(encodedText, hashedPassword):
#     # save output
#     for i in range(3):
#         encodedText = ownAlgoEncoder(encodedText, hashedPassword)


#     decodedText = encodedText

#     return decodedText

def ownAlgoDecoder(encoded_data, hashed_password):
    n = len(encoded_data)
    hashed_password_bytes = bytearray(hashed_password, "utf-8")
    decoded_data = bytearray(n)
    for i in range(n):
        decoded_data[i] = encoded_data[n - i - 1] ^ hashed_password_bytes[i % len(hashed_password_bytes)]
    
    return decoded_data


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
