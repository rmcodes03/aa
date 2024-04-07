import hashlib

def md5_hash(message):
    """Compute the MD5 hash of the given message."""
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(message.encode('utf-8'))
    return md5_hash_object.hexdigest()

if __name__ == "__main__":
    # Example usage
    message = "Risabh 4712"
    hash_result = md5_hash(message)

    print(f"Original Message: {message}")
    print(f"MD5 Hash: {hash_result}")
