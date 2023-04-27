import os
import endec

def decodeWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()

    decodedData = endec.ownAlgoDecoder(fileData, hashedPassword)
    fileDir, fileName = os.path.split(filepath)
    decodedFilepath = os.path.join(fileDir, f"{fileName[:-8]}")

    with open(decodedFilepath, "wb") as file:
        file.write(decodedData)


def encodeWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()
    encodedData = endec.ownAlgoEncoder(fileData, hashedPassword)
    encodedFilepath = filepath + ".encoded"
    with open(encodedFilepath, "wb") as file:
        file.write(encodedData)
