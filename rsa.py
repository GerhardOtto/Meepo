def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_keypair(p, q):
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


def encrypt(pk, plaintext):
    e, n = pk
    return [pow(ord(char), e, n) for char in plaintext]


def decrypt(pk, ciphertext):
    d, n = pk
    return "".join([chr(pow(char, d, n)) for char in ciphertext])


def read_binary(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binary_data

def write_binary(file_path, binary_data):
    with open(file_path, 'wb') as file:
        file.write(binary_data)

def encrypt_binary(pk, binary_data):
    e, n = pk
    byte_size = (n.bit_length() + 7) // 8
    return b"".join([pow(byte, e, n).to_bytes(byte_size, 'big') for byte in binary_data])

def decrypt_binary(pk, encrypted_data):
    d, n = pk
    byte_size = (n.bit_length() + 7) // 8
    return bytes([pow(int.from_bytes(encrypted_data[i:i+byte_size], 'big'), d, n) for i in range(0, len(encrypted_data), byte_size)])

p = 61
q = 53

public, private = generate_keypair(p, q)

def writeRSAEncrypted(file_path):
    binary_data = read_binary(file_path)
    encrypted_data = encrypt_binary(public, binary_data)
    write_binary(file_path, encrypted_data)

def writeRSADecrypted(file_path):
    encrypted_data_from_file = read_binary(file_path)
    decrypted_data = decrypt_binary(private, encrypted_data_from_file)
    write_binary(file_path, decrypted_data)