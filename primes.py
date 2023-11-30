from Crypto.Util import number

def generate_safe_prime(bit_length):
    # Generate a random (bit_length)-bit prime number
    prime_candidate = number.getPrime(bit_length)

    # Check if (prime_candidate - 1) / 2 is also a prime (safe prime)
    safe_prime_candidate = (prime_candidate - 1) >> 1
    while not number.isPrime(safe_prime_candidate):
        prime_candidate = number.getPrime(bit_length)
        safe_prime_candidate = (prime_candidate - 1) >> 1

    return prime_candidate
