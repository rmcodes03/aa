import random
import math

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular inverse of a number."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits):
    """Generate RSA key pair."""
    p, q = 0, 0

    # Step 1: Select two large prime numbers
    while not is_prime(p):
        p = random.getrandbits(bits)
    while not is_prime(q) or q == p:
        q = random.getrandbits(bits)

    # Step 2: Compute n and totient(n)
    n = p * q
    totient_n = (p - 1) * (q - 1)

    # Step 3: Select public exponent e
    e = random.randint(2, totient_n - 1)
    while gcd(e, totient_n) != 1:
        e = random.randint(2, totient_n - 1)

    # Step 4: Compute private exponent d
    d = mod_inverse(e, totient_n)

    return ((n, e), (n, d))

def encrypt(message, public_key):
    """Encrypt a message using RSA."""
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """Decrypt an encrypted message using RSA."""
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

if __name__ == "__main__":
    # Example usage
    bits = 16
    public_key, private_key = generate_keypair(bits)

    message = "Risabh Mishra"
    print("Original Message:", message)

    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)
