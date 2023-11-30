from primes import generate_safe_prime
import json
import random

def generate_params(q_bit_length):
    p = generate_safe_prime(q_bit_length)
    q = p - 1
    g = random.randint(2, p - 1)
    
    return p, q, g

if __name__ == '__main__':
    p, q, g = generate_params(512)
    params = {'p': p, 'q': q, 'g': g}
    with open('public_params.json', 'w') as f:
        json.dump(params, f, indent=4)