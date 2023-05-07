import hashlib

# Hashes password using SHA256
def hashSlingingSlasher(password):
    passwordBytes = password.encode('utf-8')
    hashObject = hashlib.sha256()
    hashObject.update(passwordBytes)
    hashedPassword = hashObject.hexdigest()

    return hashedPassword


# Encrypts binary data with own algorithm.
def ownAlgoEncoder(fileData):
    n = len(fileData)
    reorderedData = bytearray(n)

    for i in range(0, n, 2):
        if i // 2 % 2 == 0:
            reorderedData[i] = fileData[n - i - 1]
            if i + 1 < n:
                reorderedData[i + 1] = fileData[i]
        else:
            reorderedData[i] = fileData[i]
            if i + 1 < n:
                reorderedData[i + 1] = fileData[n - i - 1]

    return reorderedData


# Decrypts binary data with own algorithm.
def ownAlgoDecoder(fileData):
    n = len(fileData)
    originalData = bytearray(n)

    for i in range(0, n, 2):
        if i // 2 % 2 == 0:
            originalData[n - i - 1] = fileData[i]
            if i + 1 < n:
                originalData[i] = fileData[i + 1]
        else:
            originalData[i] = fileData[i]
            if i + 1 < n:
                originalData[n - i - 1] = fileData[i + 1]

    return originalData