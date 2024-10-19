def prime_factors_two(n):
    factors = []
    
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        n //= 2
    
    # Check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i not in factors:
                factors.append(i)
            n //= i
        if len(factors) == 2:  # Stop early if we have found two factors
            break
    
    # Check if n is a prime number greater than 2
    if n > 2 and len(factors) < 2:
        factors.append(n)

    return factors

import math

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi

def calculate_private_key(e, p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return d, n

# Main execution
if __name__ == "__main__":
    # Input public key (e, n)
    e = int(input("Enter the public exponent e: "))
    n = int(input("Enter the public modulo n: "))
    x = prime_factors_two(n)
    p=x[0]
    q=x[1]

   

    # Calculate private key
    private_key, n = calculate_private_key(e, p, q)

    print("Private Key (d):", private_key)
