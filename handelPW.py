def savePassword(hashedPassword,filePath):
    # Open a file and write the hashed password to it
    with open("password.txt", "a") as f:
        binary = readBinary(filePath)
        f.write(hashedPassword+binary + "\n" )
        

def comparePassword(hashedPassword,filePath):
    # Open the file and read each hashed password from it
    with open("password.txt", "r") as f:
        pwFile = f.readlines()

    binary = readBinary(filePath)

    # Remove any newline characters from the end of each line
    pwFile = [x.strip() for x in pwFile]

    # Compare each hashed password to the given password
    for passwords in pwFile:
        if hashedPassword+binary == passwords:
            print("Password is correct!")
            return True
    print("Password is incorrect!")
    return False


def readBinary(filePath):
    with open(filePath, "rb") as f:
        binaryData = f.read()
        first = binaryData[:5]
        last = binaryData[-5:]
    
    return (first + last).hex()