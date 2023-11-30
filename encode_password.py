from hashlib import sha256

def encode_password(password):
    ep = password.encode('utf-8')
    hp = sha256(ep).hexdigest()
    bp = int.from_bytes(ep, byteorder='big')
    return bp