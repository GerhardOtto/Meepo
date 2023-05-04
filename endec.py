import hashlib

# Hashes password using SHA256
def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')
    hashObject = hashlib.sha256()
    hashObject.update(passwordBytes)
    hashedPassword = hashObject.hexdigest()

    return hashedPassword


# Encrypts binary data with own xor algorithm.
def ownAlgoEncoder(fileData, hashedPassword):
    n = len(fileData)
    hashedPasswordBytes = bytes(hashedPassword, "utf-8")
    encodedData = bytearray(n)
    for i in range(n):
        x = fileData[n - i - 1]
        y = hashedPasswordBytes[i % len(hashedPasswordBytes)]

        encodedData[i] =  x ^ y
    
    return encodedData


# Decrypts binary data with own xor algorithm.
def ownAlgoDecoder(encodedData, hashedPassword):
    n = len(encodedData)
    hashedPasswordBytes = bytes(hashedPassword, "utf-8")
    decodedData = bytearray(n)
    for i in range(n):
        x = encodedData[i]
        y = hashedPasswordBytes[i % len(hashedPasswordBytes)]

        decodedData[n - i - 1] = x ^ y

    return decodedData


total = 0
string = hashSlingingSlasher("NOtPw")
print(string)
for char in string:
    if char.isdigit():
        total += int(char)

print("The sum of all digits in the string is:", total)