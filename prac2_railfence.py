def encrypt_rail_fence(plaintext, key):
    # Create an empty rail fence grid
    rail_fence = [[' ' for _ in range(len(plaintext))] for _ in range(key)]

    # Populate the rail fence grid with characters
    i, direction = 0, 1
    for char in plaintext:
        rail_fence[i][0] = char
        i += direction
        if i == key or i == -1:
            direction *= -1
            i += 2 * direction

    # Read characters from the rail fence grid
    ciphertext = ''.join(''.join(row) for row in rail_fence if row[0] != ' ')
    return ciphertext

def decrypt_rail_fence(ciphertext, key):
    # Create an empty rail fence grid
    rail_fence = [[' ' for _ in range(len(ciphertext))] for _ in range(key)]

    # Populate the rail fence grid with placeholder characters
    i, direction = 0, 1
    for _ in range(len(ciphertext)):
        rail_fence[i][0] = 'X'  # Placeholder character
        i += direction
        if i == key or i == -1:
            direction *= -1
            i += 2 * direction

    # Fill the rail fence grid with characters from ciphertext
    idx = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail_fence[i][j] == 'X':
                rail_fence[i][j] = ciphertext[idx]
                idx += 1

    # Read characters from the rail fence grid
    plaintext = ''
    i, direction = 0, 1
    for j in range(len(ciphertext)):
        plaintext += rail_fence[i][j]
        i += direction
        if i == key or i == -1:
            direction *= -1
            i += 2 * direction

    return plaintext

# Example usage:
plaintext = "HELLOWORLD"
key = 3

# Encryption
ciphertext = encrypt_rail_fence(plaintext, key)
print("Encrypted:", ciphertext)

# Decryption
decrypted_text = decrypt_rail_fence(ciphertext, key)
print("Decrypted:", decrypted_text)
