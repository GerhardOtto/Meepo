import os

def write(encodedText,hashedPassword):
    try:
        file = open(hashedPassword + ".txt", "w")
        file.write(encodedText)
        file.close()
    except OSError:
        print("Password already in use!")


def read(hashedPassword,filePath):
    try:
        with open(filePath, "r") as file:
            fileName = os.path.basename(filePath)
            if hashedPassword == fileName:
                encodedText = file.read()

        return encodedText

    except FileNotFoundError:
        print("Password not found!")