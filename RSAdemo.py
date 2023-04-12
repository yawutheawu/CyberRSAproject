#Derek Johnson & Maykl Yakubovsky
#2/27/2023 Cybersecurity Project - RSA encryption demo/walkthrough

import rsa as rsa
import numpy as np
import random as rand
import math as math


def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
			break
		else:
			pass
	return True


def generateKeys(bottomRange=100, topRange=500):
	#based on https://security.stackexchange.com/questions/25631/crack-plain-rsa-given-p-q-and-e and https://www.pythonpool.com/rsa-encryption-python/ and https://gist.github.com/juanplopes/6908681
	primes = [i for i in range(bottomRange, topRange) if is_prime(i)]
	p = rand.choice(primes)
	del primes[primes.index(p)]
	q = rand.choice(primes)
	phi = (p - 1) * (q - 1)
	e = rand.randint(2, phi - 1)
	while np.gcd(e, phi) != 1:
		e = rand.randint(2, phi - 1)
	n = p * q
	publicKey = [n, e]
	d = pow(e, -1, phi)
	privateKey = [n, d]
	return [publicKey, privateKey]


#https://www.geeksforgeeks.org/rsa-algorithm-cryptography/


#https://www.di-mgt.com.au/rsa_alg.html
def encryptRSA(public_key, text):
	plain = []
	for i in text:
		plain.append(ord(i))
	temp = []
	for i in plain:
		temp.append(pow(i, public_key[1], public_key[0]))
	return temp


#https://www.di-mgt.com.au/rsa_alg.html
def decryptRSA(private_key, cipherText):
	decipher = []
	for i in cipherText:
		tempHold = i**private_key[1]
		tempHold = tempHold % private_key[0]
		decipher.append(chr(tempHold))
	return decipher
