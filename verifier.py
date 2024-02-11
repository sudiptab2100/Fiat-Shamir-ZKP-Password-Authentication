import json
from hashlib import sha256
from eth_abi.packed import encode_packed

# Read the commitment & public parameters from commitment.json file
with open('commitment.json', 'r') as file:
    d = json.load(file)

commitment = d['c']
p = d['p']
q = d['q']
g = d['g']

# Read the proof from proof.json file
with open('proof.json', 'r') as file:
    proof = json.load(file)

t = proof['t']
r = proof['r']

# Verify the proof
k = 0
hash_message = encode_packed(['uint256', 'uint256', 'uint256', 'uint256'], [g, commitment, t, k])
c = int(sha256(hash_message).hexdigest(), 16)
t1 = (pow(g, r, p) * pow(commitment, c, p)) % p
print("Valid:", t == t1)