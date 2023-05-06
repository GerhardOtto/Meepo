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
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

# Modular Inverse
def mod_inverse(e, phi):
    _, x, _ = extended_gcd(e, phi)
    return (x % phi + phi) % phi

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random prime number
def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        if is_prime(n):
            return n

# Generate RSA keys
def generate_rsa_keys(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
            
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# RSA encryption
def encrypt_rsa(plaintext, public_key):
    n, e = public_key
    return pow(plaintext, e, n)

# RSA decryption
def decrypt_rsa(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)


def store_keys(binary,password, public_key, private_key):
    with open('keys.txt', 'a') as keys_file:
        keys_file.write(f"{binary}!{password}: {public_key[0]},{public_key[1]};{private_key[0]},{private_key[1]}\n")

def getPrivateKey(password):
    with open('keys.txt', 'r') as keys_file:
        for line in keys_file:
            binary_and_password, keys = line.strip().split(': ')
            binary, stored_password = binary_and_password.split('!')
            if stored_password == password:
                _, private_key_str = keys.split(';')
                n, d = [int(x) for x in private_key_str.split(',')]
                return binary, (n, d)
            else :
                return None, None



def encrypt_file(input_filepath, public_key):
    output_filepath = f"{input_filepath}.encrypted"
    with open(input_filepath, 'rb') as infile:
        content = infile.read()
        encrypted_content = [encrypt_rsa(byte, public_key) for byte in content]

    with open(output_filepath, 'w') as outfile:
        outfile.write(','.join(str(x) for x in encrypted_content))

    return handelPW.readBinary(output_filepath)

# Decrypt a file
def decrypt_file(input_filepath, private_key):
    output_filepath = f"{os.path.splitext(input_filepath)[0]}"
    with open(input_filepath, 'r') as infile:
        encrypted_content = [int(x) for x in infile.read().split(',')]

    decrypted_content = bytearray([decrypt_rsa(byte, private_key) for byte in encrypted_content])

    with open(output_filepath, 'wb') as outfile:
        outfile.write(decrypted_content)