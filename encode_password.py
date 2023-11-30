from hashlib import sha256

def encode_password(password):
    ep = password.encode('utf-8')
    hp = sha256(ep).hexdigest()
    return int(hp, 16)
