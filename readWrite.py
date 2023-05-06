import os
import endec

# Delete a file
def deleteFile(filepath):
    os.remove(filepath)

# Write decoded data to file.
def decryptWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()

    decodedData = endec.ownAlgoDecoder(fileData, hashedPassword)
    fileDir, fileName = os.path.split(filepath)
    decodedFileName = fileName[:-len(".encrypted")]
    decodedFilepath = os.path.join(fileDir, decodedFileName)

    return decodedFilepath,decodedData


# Write encoded data to file.
def encryptWithOwnAlgo(filepath, hashedPassword):
    with open(filepath, "rb") as file:
        fileData = file.read()
    encodedData = endec.ownAlgoEncoder(fileData, hashedPassword)
    encodedFilepath = filepath + ".encrypted"

    with open(encodedFilepath, "wb") as file:
        file.write(encodedData)

    return encodedFilepath