import json
import random
from encode_password import encode_password
from hashlib import sha256

# Read the public parameters from public_params.json file
with open('public_params.json', 'r') as file:
    public_params = json.load(file)

p = public_params['p']
q = public_params['q']
g = public_params['g']

# Read the public commitment from commitment.json file
with open('commitment.json', 'r') as file:
    commitment = json.load(file)['c']

def generate_proof(password):
    x = encode_password(password)
    v = random.randint(1, q)
    t = pow(g, v, p)
    hash_message = str(g) + str(commitment) + str(t)
    c = int(sha256(hash_message.encode()).hexdigest(), 16)
    r = (v - c * x) % q
    
    proof = {
        't': t,
        'r': r
    }
    
    # Write the proof to proof.json file
    with open('proof.json', 'w') as file:
        json.dump(proof, file, indent=4)

password = "pAs$word987654321p"
generate_proof(password)