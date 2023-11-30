def encode_password(password):
    ep = password.encode('utf-8')
    bp = int.from_bytes(ep, byteorder='big')
    return bp

def decode_password(bp):
    ep = bp.to_bytes((bp.bit_length() + 7) // 8, byteorder='big')
    password = ep.decode('utf-8')
    return password
