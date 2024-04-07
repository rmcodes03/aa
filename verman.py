import base64

def vernam_cipher(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must have the same length")

    ciphertext_bytes = bytes(ord(p) ^ ord(k) for p, k in zip(plaintext, key))
    ciphertext_base64 = base64.b64encode(ciphertext_bytes).decode('utf-8')
    return ciphertext_base64

def vernam_decipher(ciphertext_base64, key):
    ciphertext_bytes = base64.b64decode(ciphertext_base64)
    decrypted_text = ''.join(chr(c ^ ord(k)) for c, k in zip(ciphertext_bytes, key))
    return decrypted_text

# Example usage:
plaintext = "RISABHMISHRA"
key = "SECRETKEYSEC"  # Key must be as long as the plaintext

# Encryption
ciphertext = vernam_cipher(plaintext, key)
print("Plaintext:", plaintext)
print("Key      :", key)
print("Encrypted:", ciphertext)

# Decryption (using the same key)
decrypted_text = vernam_decipher(ciphertext, key)
print("Decrypted:", decrypted_text)
