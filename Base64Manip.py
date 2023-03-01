import base64

def touchBase(filePath):
    with open(filePath, 'rb') as file:
        fileContents = file.read()

    encodedContents = base64.b64encode(fileContents)

    return encodedContents.decode('utf-8')


def leaveBase(filePath):
    with open(filePath, 'r') as file:
        fileContents = file.read()

    decodedContents = base64.b64decode(fileContents).decode('utf-8')

    return decodedContents