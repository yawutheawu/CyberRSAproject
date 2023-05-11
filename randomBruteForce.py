#Brute Force Decrypting RSA

#https://www.di-mgt.com.au/rsa_alg.html

import RSAdemo
import time

message = "Unciphered"
real_public_key = [21473, 3265]  #generated numbers
real_private_key = [21473, 8545]  #generated numbers

cipherText = RSAdemo.encryptRSA(real_public_key, message)

#make a private generation in this file alone, so that it can be tested without interfering with the main or RSAdemo


#FIX: try except needs to go for the generation, the printing is not the problem
def makeGuess():
	keys = RSAdemo.generateKeys()
	used_keys = []
	private_key = keys[1]
	used_keys.append(private_key)
	public_key = real_public_key
	ideal_message = ""
	for i in message:
		ideal_message += str(i)
	generation = decryptRSA(private_key, cipherText)
	try:
		print("\n ideal: " + str(ideal_message) + ", generation: " + str(generation))
	except:
		print("\n Generated Invalid Unicode Character")

	while (generation != ideal_message):
		print("Not Found Yet! Attempted Crack: " + str(generation))
		keys = RSAdemo.generateKeys()
		while (keys[1] in used_keys):
			keys = RSAdemo.generateKeys()
		private_key = keys[1]
		used_keys.append(private_key)
		generation = decryptRSA(private_key, cipherText)
	print("\n Brute Forced Successfully")
	print("\n ideal: " + str(ideal_message) + ", generation: " + str(generation))
	return True


def prime_factor(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
	return n


def primeFactorizor(cipherText, publicKey, realText):
	print("\n Factoring.", end="")
	primeFactors = prime_factor(publicKey[0])
	print(".", end="")
	primeFactors2 = int(publicKey[0] / primeFactors)
	print(".")
	print(primeFactors)
	print(primeFactors2)
	phi = (primeFactors - 1) * (primeFactors2 - 1)
	if publicKey[1] > 2 and publicKey[1] < (phi - 1):
		print("\n Phi check success!")
	d = pow(publicKey[1], -1, phi)
	unchipher = decryptRSA([primeFactors * primeFactors2, d], cipherText)
	decipher = ""
	for i in unchipher:
		decipher += i
	if decipher == realText:
		print("\n Complete: Deciphered text: " + str(decipher) +
		      " , original text: " + str(realText))
	else:
		print("\n Incomplete: Deciphered text: " + str(decipher) +
		      " , original text: " + str(realText))


#privatekey = (key_pair 1) = [n, d]  = brute force senders private key


def primeGuesser(cipherText, publicKey):
	print("\n Factoring.", end="")
	primeFactors = prime_factor(publicKey[0])
	print(".", end="")
	primeFactors2 = int(publicKey[0] / primeFactors)
	print(".")
	print(primeFactors)
	print(primeFactors2)
	phi = (primeFactors - 1) * (primeFactors2 - 1)
	if publicKey[1] > 2 and publicKey[1] < (phi - 1):
		print("\n Phi check success!")
	d = pow(publicKey[1], -1, phi)
	unchipher = decryptRSA([primeFactors * primeFactors2, d], cipherText)
	decipher = ""
	for i in unchipher:
		decipher += i
	print("\n Guess: " + str(decipher))


#https://www.di-mgt.com.au/rsa_alg.html
def decryptRSA(private_key, cipherText):
	decipher = []
	for i in cipherText:
		tempHold = i**private_key[1]
		tempHold %= private_key[0]
		decipher.append(chr(tempHold))
		print(chr(tempHold), end=" ")
	print()
	return decipher


def primeTimer(realText, x=200, y=500):
	import timeCalc
	startTime = time.time()
	keyPair = RSAdemo.generateKeys(x, y)
	publicKey = keyPair[0]
	cipherText = RSAdemo.encryptRSA(publicKey, realText)
	primeFactors = prime_factor(publicKey[0])
	primeFactors2 = int(publicKey[0] / primeFactors)
	print(primeFactors)
	print(primeFactors2)
	phi = (primeFactors - 1) * (primeFactors2 - 1)
	d = pow(publicKey[1], -1, phi)
	unchipher = decryptRSA([primeFactors * primeFactors2, d], cipherText)
	decipher = ""
	for i in unchipher:
		decipher += i
	if decipher == realText:
		endTime = time.time()
		timeCalc.addToHack(publicKey[0], (endTime - startTime))
	else:
		print("unsuccessful")
