import numpy as np
from sympy import Matrix, mod_inverse

def matrix_mod_inv(matrix, modulus):
    det = Matrix(matrix).det() % modulus
    det_inv = mod_inverse(det, modulus)
    
    if det_inv is None:
        raise ValueError("The key matrix is not invertible modulo {}".format(modulus))

    adj = Matrix(matrix).adjugate()
    inv = (det_inv * adj) % modulus
    return np.array(inv, dtype=int)

def matrix_to_numbers(matrix):
    return [ord(char) - ord('A') for char in matrix.flatten()]

def numbers_to_matrix(numbers, shape):
    return np.array([chr(num % 26 + ord('A')) for num in numbers]).reshape(shape)

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    plaintext_matrix = np.array([ord(char) - ord('A') for char in plaintext]).reshape(-1, 2)
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26

    ciphertext = ''.join([chr(num + ord('A')) for num in ciphertext_matrix.flatten()])
    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace(" ", "")
    
    ciphertext_matrix = np.array([ord(char) - ord('A') for char in ciphertext]).reshape(-1, 2)
    
    # Check if the determinant is invertible (not divisible by 26)
    if Matrix(key_matrix).det() % 26 == 0:
        raise ValueError("The key matrix is not invertible modulo 26")

    key_matrix_inv = matrix_mod_inv(key_matrix, 26)
    plaintext_matrix = np.dot(ciphertext_matrix, key_matrix_inv) % 26

    plaintext = ''.join([chr(num + ord('A')) for num in plaintext_matrix.flatten()])
    return plaintext

# Example usage:
key_matrix = np.array([[3, 10], [20, 9]])  # Example of an invertible key matrix
plaintext = "MISHRARISABH"
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)

print("Plaintext:", plaintext)
print("Key Matrix:")
print(key_matrix)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
