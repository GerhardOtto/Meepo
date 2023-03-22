import base64

def encodeToBinary(filePath):
    with open(filePath, 'rb') as file:
        fileContents = file.read()

    return fileContents


def decodeFromBinary(filePath):
    with open(filePath, 'r') as file:
        fileContents = file.read()

    decodedBinary = fileContents.decode()

    return decodedBinary