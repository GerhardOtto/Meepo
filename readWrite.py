import os
import endec

def decodeWithOwnAlgo(filepath, hashedPassword, decoded_filepath='~/Desktop/decoded_file'):
    if not decoded_filepath.endswith('.txt'):
        decoded_filepath += '.txt'
    decoded_filepath = os.path.expanduser(decoded_filepath)

    with open(filepath, "rb") as file:
        fileData = file.read()

    decodedData = endec.ownAlgoDecoder(fileData, hashedPassword)

    with open(decoded_filepath, "wb") as file:
        file.write(decodedData)



def encodeWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()

    encodedData = endec.ownAlgoEncoder(fileData, hashedPassword)

    encodedFilepath = filepath + ".encoded"
    with open(encodedFilepath, "wb") as file:
        file.write(encodedData)

def writeEncodedText(encodedText,hashedPassword):
    try:
        file = open(hashedPassword + ".txt", "w+")
        file.write(encodedText)
        file.close()
    except OSError:
        print("Password already in use!")


def readEncodedText(hashedPassword, filePath):
    try:
        with open(filePath, "r") as file:
            fileName = os.path.basename(filePath)
            encodedText = file.read()
            if hashedPassword == fileName:
                encodedText = file.read()

        return encodedText

    except FileNotFoundError:
        print("Password not found!")
