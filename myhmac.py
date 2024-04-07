import hmac
import hashlib

def generate_hmac(message, secret_key):
    """Generate HMAC signature for the given message and secret key."""
    hmac_signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
    return hmac_signature.hexdigest()

def verify_hmac(message, secret_key, provided_signature):
    """Verify HMAC signature for the given message, secret key, and provided signature."""
    calculated_signature = generate_hmac(message, secret_key)
    return hmac.compare_digest(calculated_signature, provided_signature)

if __name__ == "__main__":
    # Example usage
    secret_key = "secret_key"
    message = "Hello Risabh Mishra!"

    # Generate HMAC signature
    hmac_signature = generate_hmac(message, secret_key)
    print(f"HMAC Signature: {hmac_signature}")

    # Verify HMAC signature
    is_valid = verify_hmac(message, secret_key, hmac_signature)
    if is_valid:
        print("HMAC Signature is valid.")
    else:
        print("HMAC Signature is not valid.")
