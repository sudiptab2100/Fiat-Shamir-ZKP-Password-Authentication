import json
from encode_password import encode_password

# Read the contents of public_params.json file
with open('public_params.json', 'r') as file:
    public_params = json.load(file)

p = public_params['p']
q = public_params['q']
g = public_params['g']

def generate_commitment(password):
    ep = encode_password(password)
    commitment = {'c': pow(g, ep, p), 'p': p, 'q': q, 'g': g}
    
    with open('commitment.json', 'w') as f:
        json.dump(commitment, f, indent=4)

password = "pAs$word987654321p"
generate_commitment(password)