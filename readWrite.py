import os

def writeEncodedText(encodedText,hashedPassword):
    try:
        file = open(hashedPassword + ".txt", "w")
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
