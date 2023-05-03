# Encoding and decoding binary files

def encodeToBinary(filePath):
    with open(filePath, 'rb') as file:
        fileContents = file.read()
        print(fileContents)

    return fileContents


def decodeFromBinary(filePath):
    with open(filePath, 'r') as file:
        fileContents = file.read()

    decodedBinary = fileContents.decode()

    return decodedBinary