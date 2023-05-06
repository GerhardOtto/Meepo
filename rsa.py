import random
import math
import os
import handelPW

# Greatest Common Divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm
def extendedGcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extendedGcd(b % a, a)
        return g, y - (b // a) * x, x

# Modular Inverse
def modInverse(e, phi):
    _, x, _ = extendedGcd(e, phi)
    return (x % phi + phi) % phi

# Check if a number is prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random prime number
def generatePrime(bits):
    while True:
        n = random.getrandbits(bits)
        if isPrime(n):
            return n

# Generate RSA keys
def generateRsaKeys(bits):
    p = generatePrime(bits // 2)
    q = generatePrime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
            
    d = modInverse(e, phi)
    return (n, e), (n, d)

# RSA encryption
def encryptRsa(plaintext, publicKey):
    n, e = publicKey
    return pow(plaintext, e, n)

# RSA decryption
def decryptRsa(ciphertext, privateKey):
    n, d = privateKey
    return pow(ciphertext, d, n)


def storeKeys(binary,password, publicKey, privateKey):
    with open('keys.txt', 'a') as keys_file:
        keys_file.write(f"{binary}!{password}: {publicKey[0]},{publicKey[1]};{privateKey[0]},{privateKey[1]}\n")

def getPrivateKey(password):
    with open('keys.txt', 'r') as keys_file:
        for line in keys_file:
            binaryAndPassword, keys = line.strip().split(': ')
            binary, storedPassword = binaryAndPassword.split('!')
            if storedPassword == password:
                _, privateKey_str = keys.split(';')
                n, d = [int(x) for x in privateKey_str.split(',')]
                return binary, (n, d)
            else :
                return None, None



def encryptFile(inputFilepath, publicKey):
    outputFilepath = f"{inputFilepath}.encrypted"
    with open(inputFilepath, 'rb') as infile:
        content = infile.read()
        encryptedContent = [encryptRsa(byte, publicKey) for byte in content]

    with open(outputFilepath, 'w') as outfile:
        outfile.write(','.join(str(x) for x in encryptedContent))

    return handelPW.readBinary(outputFilepath)

# Decrypt a file
def decryptFile(inputFilepath, privateKey):
    outputFilepath = f"{os.path.splitext(inputFilepath)[0]}"
    with open(inputFilepath, 'r') as infile:
        encryptedContent = [int(x) for x in infile.read().split(',')]

    decryptedContent = bytearray([decryptRsa(byte, privateKey) for byte in encryptedContent])

    with open(outputFilepath, 'wb') as outfile:
        outfile.write(decryptedContent)