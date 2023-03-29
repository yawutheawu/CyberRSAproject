#Realistically doesn't work, but fun to have here ig

import random


# Generate large random primes p and q
def generate_prime(bits):
	while True:
		p = random.getrandbits(bits)
		if is_prime(p):
			return p


def is_prime(n, k=5):
	if n <= 3:
		return n == 2 or n == 3
	for i in range(k):
		a = random.randint(2, n - 2)
		x = pow(a, n - 1, n)
		if x != 1:
			return False
	return True


def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a


def extended_gcd(a, b):
	if b == 0:
		return a, 1, 0
	d, x, y = extended_gcd(b, a % b)
	return d, y, x - (a // b) * y


# Generate RSA keys
def generate_keys(bits):
	p = generate_prime(bits // 2)
	q = generate_prime(bits // 2)
	N = p * q
	phi = (p - 1) * (q - 1)
	e = random.randint(2, phi - 1)
	while gcd(e, phi) != 1:
		e = random.randint(2, phi - 1)
	d, _, _ = extended_gcd(e, phi)
	d %= phi
	return (e, N), (d, N)


# Encrypt and decrypt messages
def encrypt(message, public_key):
	e, N = public_key
	m = int.from_bytes(message.encode(), byteorder='big')
	if m >= N:
		raise ValueError('message too large')
	return pow(m, e, N)


def decrypt(ciphertext, private_key):
	d, N = private_key
	m = pow(ciphertext, d, N)
	message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
	return message.decode()


# Generate keys and encrypt/decrypt message
if __name__ == '__main__':
	public_key, private_key = generate_keys(2048)
	message = 'awooga'
	ciphertext = encrypt(message, public_key)
	plaintext = decrypt(ciphertext, private_key)
	print('Public key:', public_key)
	print('Private key:', private_key)
	print('Encrypted message:', ciphertext)
	print('Decrypted message:', plaintext)
