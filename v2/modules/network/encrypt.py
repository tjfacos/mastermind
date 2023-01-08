import hashlib

def encrypt(text):
    result = hashlib.sha512(text.encode())
    return result.hexdigest()
