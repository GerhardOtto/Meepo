import os
import endec

def deleteFile(filepath):
    os.remove(filepath)

def decodeWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()

    decodedData = endec.ownAlgoDecoder(fileData, hashedPassword)
    fileDir, fileName = os.path.split(filepath)
    decodedFileName = fileName[:-len(".encoded")]
    decodedFilepath = os.path.join(fileDir, decodedFileName)

    with open(decodedFilepath, "wb") as file:
        file.write(decodedData)


def encodeWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()
    encodedData = endec.ownAlgoEncoder(fileData, hashedPassword)
    encodedFilepath = filepath + ".encoded"

    with open(encodedFilepath, "wb") as file:
        file.write(encodedData)

    return encodedFilepath

