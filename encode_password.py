from hashlib import sha256
from eth_abi.packed import encode_packed

def encode_password(password):
    ep = encode_packed(['string'], [password])
    hp = sha256(ep).hexdigest()
    return int(hp, 16)
