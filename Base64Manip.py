import base64

def touchBase(filePath):
    # Open the text file in binary mode and read its contents
    with open(filePath, 'rb') as file:
        fileContents = file.read()

    # Encode the file contents to base64
    encodedContents = base64.b64encode(fileContents)

    # Convert the bytes to a string and return the result
    return encodedContents.decode('utf-8')


def leaveBase(filePath):
    # Open the text file and read its contents
    with open(filePath, 'r') as file:
        fileContents = file.read()

    # Decode the base64-encoded contents of the file
    decodedContents = base64.b64decode(fileContents).decode('utf-8')

    # Return the decoded contents as a string
    return decodedContents