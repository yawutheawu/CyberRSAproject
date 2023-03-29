#Derek Johnson & Maykl Yakubovsky 
#2/14/2023 Cybersecurity Project
import RSAdemo
import randomBruteForce
import Messages as m1
#RSA Demo


def struct():
	text = input(
	 "Are you running demo(1), Generating messenger keypairs(2), messager(3), or random brute force(4)?: "
	)
	try:
		text = int(text)
	except:
		print("Please input a number")
		struct()
	if (text == 1):
		keyPair = RSAdemo.generateKeys()
		public_key = keyPair[0]
		private_key = keyPair[1]
		print(keyPair)
		message = "The Linux Ever"
		encrypted = RSAdemo.encryptRSA(public_key, message)
		decrypted = RSAdemo.decryptRSA(private_key, encrypted)
		str_dec = ""
		for i in decrypted:
			str_dec += i
		print("Actual Message: " + message)
		encrypted = RSAdemo.encryptRSA(public_key, message)
		print("Encrypted Message: " + str(encrypted))
		decrypted = RSAdemo.decryptRSA(private_key, encrypted)
		print("Decrypted Message: " + str(decrypted))
	elif (text == 2):
		SenderKeypair = RSAdemo.generateKeys()
		RecieverKeypair = RSAdemo.generateKeys()
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
		elif (text == 2):
			realText = "spoiler alert, numbers are sometimes real and sometimes not"
			keyPair = RSAdemo.generateKeys(1000, 5000)
			publicKey = keyPair[0]
			private_key = keyPair[1]  #just in case
			cipherText = RSAdemo.encryptRSA(publicKey, realText)
			randomBruteForce.primeFactorizor(cipherText, publicKey, realText)
		else:
			print("not an option")
			struct()
	else:
		print("Not an option")
		struct()


struct()
