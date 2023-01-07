import hashlib

def encrypt(text):
    result = hashlib.sha512(text.encode())
    return result.hexdigest()

if __name__ == "__main__":
    print(encrypt(encrypt("password123")))