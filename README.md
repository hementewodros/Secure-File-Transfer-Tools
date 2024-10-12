# Secure-File-Transfer-NotDone
# 1) RSA Key Generation Script

## Overview

This script implements a simple RSA key generation algorithm. It prompts the user for two prime numbers, calculates the public and private keys based on those inputs, and checks for input validity.

## Features

- Validates whether the input numbers are prime.
- Calculates the public and private keys using RSA algorithm.
- Provides error messages for invalid inputs.

## Requirements

- Python 3.x
- No external libraries are required.

## How It Works

1. **Prime Check**: The script first checks if the entered numbers \( p \) and \( q \) are prime.
2. **Public Key Calculation**: It calculates the public key using the formula \( n = p \times q \) and selects a suitable \( e \) such that \( e \) is coprime to \( (p-1)(q-1) \).
3. **Private Key Calculation**: It calculates the private key \( d \) using the modular multiplicative inverse of \( e \).
4. **Error Handling**: If the input numbers are not positive or not prime, it provides an appropriate error message.

## Functions

- `checkIfPrime(a)`: Checks if a number is prime.
- `calculatePbKey(p, q)`: Calculates the public key.
- `calculatePvKey(e, En, n)`: Calculates the private key.
- `error(a)`: Displays error messages based on the input.

## Usage

1. Run the script.
2. Enter a prime number for \( p \) when prompted.
3. Enter a prime number for \( q \) when prompted.
4. The script will output the public and private keys if both inputs are valid.

### Example

```
p: 61
q: 53
Good Job!
Public Key: (e, n)
Private Key: (d, n)
```

## Notes

- Ensure that the numbers you enter are prime; otherwise, the script will prompt an error.
- The range for calculating the private key can be adjusted for larger values if necessary.

## Author

This script was created as an educational demonstration of the RSA algorithm. 

## License

This script is provided for educational purposes. Feel free to use and modify it as needed!
