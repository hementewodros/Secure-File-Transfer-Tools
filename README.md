# Secure File Transfer

Welcome to the Secure File Transfer repository! This project implements a basic encryption and decryption system using RSA (Rivest-Shamir-Adleman) cryptography. The system allows users to encrypt and decrypt numbers, which can be adapted for securing sensitive data.

## Features

- **RSA Encryption**: Generate public and private keys for encrypting and decrypting data.
- **Prime Checking**: Validate input numbers to ensure they are prime.
- **Random Key Selection**: Choose random valid encryption keys from a generated list.
- **User-friendly Input**: Simple command-line interface for user inputs.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secure-file-transfer.git
   cd secure-file-transfer
   ```

2. Run the encryption and decryption script:
   ```bash
   python encrypt_decrypt_numbers.py
   ```

### Usage

1. Input two prime numbers `p` and `q` when prompted.
2. The program will generate public and private keys based on these primes.
3. You can then input a number to encrypt or decrypt using the generated public key.

### Example

```plaintext
p: 61
q: 53
Good Job!
Public Key: (17, 3233)
Private Key: (2753, 3233)
Encryption Key in the form of (e, En): (17, 3233)
Number that you want to encrypt/decrypt: 65
Encrypted Number: 2790
```

## Functions Overview

- **checkIfPrime(a)**: Checks if the given number `a` is a prime number.
- **calculatePbKey(p, q)**: Computes the public key based on the two prime numbers `p` and `q`.
- **calculatePvKey(e, En, n)**: Calculates the private key.
- **error(a)**: Handles error messages for non-positive or non-prime inputs.

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss potential improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For any questions or feedback, please reach out via GitHub issues. Happy coding!
