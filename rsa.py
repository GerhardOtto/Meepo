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


def generate_public_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    return (e, n)


def generate_private_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return (d, n)


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

def encrypt_binary(pk, data):
    e, n = pk
    size = (n.bit_length() + 7) // 8
    encrypted_data = []

    for b in data:
        encrypted_byte = pow(b, e, n).to_bytes(size, 'big')
        encrypted_data.append(encrypted_byte)

    encrypted_binary = b"".join(encrypted_data)
    return encrypted_binary

def decrypt_binary(pk, encrypted_data):
    d, n = pk
    size = (n.bit_length() + 7) // 8
    decrypted_data = []

    for i in range(0, len(encrypted_data), size):
        chunk = encrypted_data[i:i+size]
        decrypted_byte = pow(int.from_bytes(chunk, 'big'), d, n)
        decrypted_data.append(decrypted_byte)

    decrypted_binary = bytes(decrypted_data)
    return decrypted_binary


p = 11
q = 17


def writeRSAEncrypted(filePath, p = 11, q = 17):
    binary = read_binary(filePath)
    public= generate_public_key(p, q)
    encrypted = encrypt_binary(public, binary)
    write_binary(filePath, encrypted)


def writeRSADecrypted(file_path, p = 11, q = 17):
    encrypted_data_from_file = read_binary(file_path)
    private = generate_private_key(p, q)
    decrypted_data = decrypt_binary(private, encrypted_data_from_file)
    write_binary(file_path, decrypted_data)