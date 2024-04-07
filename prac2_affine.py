import math

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt_affine(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((a * (ord(char) - 65) + b) % 26 + 65)
            else:
                ciphertext += chr((a * (ord(char) - 97) + b) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def decrypt_affine(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((a_inv * (ord(char) - 65 - b)) % 26 + 65)
            else:
                plaintext += chr((a_inv * (ord(char) - 97 - b)) % 26 + 97)
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = "RISABH"
a, b = 17, 20
ciphertext = encrypt_affine(plaintext, a, b)
decrypted_text = decrypt_affine(ciphertext, a, b)

print("Plaintext:", plaintext)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)
