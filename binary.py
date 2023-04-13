import base64

def encodeToBinary(filePath):
    with open(filePath, 'rb') as file:
        fileContents = file.read()
        # fileContents = fileContents.__bytes__()
        #how to encode string to binary
        print(fileContents)
        # fileContents = base64.b64encode(fileContents)

    return fileContents


def decodeFromBinary(filePath):
    with open(filePath, 'r') as file:
        fileContents = file.read()

    decodedBinary = fileContents.decode()

    return decodedBinary