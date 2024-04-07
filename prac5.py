import random

def generate_key(p, g, private_key):
    """Generate Diffie-Hellman key."""
    return pow(g, private_key, p)

def diffie_hellman(p, g):
    """Perform Diffie-Hellman key exchange."""
    # Risabh and Sydney each choose a private key
    risabh_private_key = random.randint(2, p - 1)
    sydney_private_key = random.randint(2, p - 1)

    # Compute public keys
    risabh_public_key = generate_key(p, g, risabh_private_key)
    sydney_public_key = generate_key(p, g, sydney_private_key)

    # Exchange public keys
    shared_key_risabh = generate_key(p, sydney_public_key, risabh_private_key)
    shared_key_sydney = generate_key(p, risabh_public_key, sydney_private_key)

    return shared_key_risabh, shared_key_sydney

if __name__ == "__main__":
    # Common parameters (p and g)
    p = 23  # Prime number
    g = 4   # Primitive root modulo p

    # Perform Diffie-Hellman key exchange
    shared_key_risabh, shared_key_sydney = diffie_hellman(p, g)

    # Display results
    print("Common Prime (p):", p)
    print("Common Primitive Root (g):", g)
    print("\nRisabh's Private Key:", shared_key_risabh)
    print("Sydney's Private Key:", shared_key_sydney)
