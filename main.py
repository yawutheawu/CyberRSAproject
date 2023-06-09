#Derek Johnson & Maykl Yakubovsky
#2/14/2023 Cybersecurity Project
import RSAdemo
import randomBruteForce
import Messages as m1
import time
import timeCalc
import mergeDicts
#RSA Demo
testingText = r"030-88-62**"

def struct():
	text = input(
	 "Are you running demo(1), Generating messenger keypairs(2), messager(3), random brute force(4), or do a runtime estimate(5)?: "
	)
	try:
		text = int(text)
	except:
		print("Please input a number")
		struct()
	if (text == 1):
		RSAdemo.forReps(300, 700)
		struct()
	elif (text == 2):
		SenderKeypair = RSAdemo.generateKeys(250, 500)
		RecieverKeypair = RSAdemo.generateKeys(250, 500)
		print()
		print("Person 1 N: " + str(SenderKeypair[0][0]))
		print("Person 1 public key: " + str(SenderKeypair[0][1]))
		print("Person 1 private key: " + str(SenderKeypair[1][1]))
		print()
		print("Person 2 N: " + str(RecieverKeypair[0][0]))
		print("Person 2 public key: " + str(RecieverKeypair[0][1]))
		print("Person 2 private key: " + str(RecieverKeypair[1][1]))
		print()
		print("generated keypairs")
		struct()
	elif (text == 3):
		m1.inputs()
		m1.userloop_structure()
		struct()
	elif (text == 4):
		text = input(
		 "Do you want random guesser(1) or factor based brute force(2)?: ")
		try:
			text = int(text)
		except:
			print("input a number")
			struct()
		if (text == 1):
			broken = False
			while (not broken):
				broken = randomBruteForce.makeGuess()
			struct()
		elif (text == 2):
			keyPair = RSAdemo.generateKeys(5000, 10000)
			publicKey = keyPair[0]
			private_key = keyPair[1]  #just in case
			cipherText = RSAdemo.encryptRSA(publicKey, testingText)
			print("Cipertext: " + str(cipherText))
			randomBruteForce.primeFactorizor(cipherText, publicKey, testingText)
			struct()
		elif (text == 2):
			keyPair = RSAdemo.generateKeys(5000, 10000)
			publicKey = keyPair[0]
			private_key = keyPair[1]  #just in case
			cipherText = RSAdemo.encryptRSA(publicKey, testingText)
			print("Cipertext: " + str(cipherText))
			randomBruteForce.primeFactorizor(cipherText, publicKey, testingText)
			struct()
		else:
			print("not an option")
			struct()
	elif (text == 5):
		text = input(
		 "Do you want to estimate encrypt/decrypt (1) or brute force attacks (2)?: ")
		try:
			text = int(text)
		except:
			print("input a number")
			struct()
		if text == 1:
			timeCalc.estimate(testingText)
			struct()
		if text == 2:
			timeCalc.fellasBeHacking(testingText)
			struct()
	else:
		print("Not an option")
		struct()


struct()
