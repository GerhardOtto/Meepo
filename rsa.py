import random

# create greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# create modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# determine if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# generate public and private keys
def generateKeypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


# encrypt plaintext
def encrypt(publicKey, plainText):
    e, n = publicKey
    cipherText = [pow(ord(char), e, n) for char in plainText]

    return cipherText


# decrypt ciphertext
def decrypt(publicKey, cipherText):
    d, n = publicKey
    plainText = "".join([chr(pow(char, d, n)) for char in cipherText])

    return plainText


# Read binary data from file.
def readBinary(filepath):
    with open(filepath, 'rb') as file:
        binaryData = file.read()

    return binaryData

# Write binary data to file.
def writeBinary(filepath, binaryData):
    with open(filepath, 'wb') as file:
        file.write(binaryData)


# Encrypts binary data with public key.
def encryptBinary(publicKey, binaryData):
    e, n = publicKey
    byteSize = (n.bit_length() + 7) // 8

    return b"".join([pow(byte, e, n).to_bytes(byteSize, 'big') for byte in binaryData])

# Decrypts binary data with public key.
def decryptBinary(publicKey, encryptedData):
    d, n = publicKey
    byteSize = (n.bit_length() + 7) // 8

    return bytes([pow(int.from_bytes(encryptedData[i:i+byteSize], 'big'), d, n) for i in range(0, len(encryptedData), byteSize)])


# Generate prime from seed
# def generatePrimeFromSeed(seed, start=0):
#     random.seed(seed)
#     i = start
#     while True:
#         if is_prime(i):
#             return i
#         i += random.randint(1, 1000)

def generatePrimeFromSeed(seed, start=2):
    num = seed + start
    while not is_prime(num):
        num += 1
    return num

# Generate public prime from password
def generatePublicPrimesFromPassword(hashedPassword):
    hashValue = int(hashedPassword, 16)
    public = generatePrimeFromSeed(hashValue)
    print("Generated public prime: " + str(public))
    return public


# Generate private prime from password and public prime
def generatePrivatePrimesFromPassword(hashedPassword,public):
    hashValue = int(hashedPassword, 16)
    private = generatePrimeFromSeed(hashValue, start=public+1)
    print("Generated private prime: " + str(private))
    return private


# Write RSA encrypted data to file
def writeRSAEncrypted(filepath, public):
    binaryData = readBinary(filepath)
    encryptedData = encryptBinary(public, binaryData)
    writeBinary(filepath, bytearray(encryptedData))

# Write RSA decrypted data to file
def writeRSADecrypted(filepath, private):
    encryptedDataFromFile = readBinary(filepath)
    decryptedData = decryptBinary(private, encryptedDataFromFile)
    writeBinary(filepath, decryptedData)


# Sample usage
# p = 61
# q = 53

# public, private = generateKeypair(p, q)

# def writeRSAEncrypted(filepath):
#     binaryData = readBinary(filepath)
#     encryptedData = encryptBinary(public, binaryData)
#     writeBinary(filepath, encryptedData)

# def writeRSADecrypted(filepath):
#     encryptedDataFromFile = readBinary(filepath)
#     decryptedData = decryptBinary(private, encryptedDataFromFile)
#     writeBinary(filepath, decryptedData)