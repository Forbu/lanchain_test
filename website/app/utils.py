import hashlib

def hash_password(password):
    """Hashes a password using the SHA-256 algorithm."""
    salt = 'freelawishere'  # Replace with a random string of characters
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password
