import RSAdemo

personalKeypair = []
recipentKeypair = []


def inputs():
	try:
		global personalKeypair
		global recipentKeypair
		Personal_N = int(input("Copy and paste user N: "))
		d = int(input("Copy and paste user private key: "))
		personalKeypair = [Personal_N, d]
		Public_N = int(input("Copy and paste recipient N: "))
		Public_E = int(input("Copy and paste recipient public key: "))
		recipentKeypair = [Public_N, Public_E]
	except:
		print("Some input was incorrect, please try again")
		inputs()


def userloop_structure():
	userChoice = input(
	 "Are you encrypting a message to send, or decrypting a message you received? "
	)
	if "encrypt" in userChoice:
		text = input("What is the text you would like to encrypt: ")
		print("The ciphertext to send is: " +
		      str(RSAdemo.encryptRSA(recipentKeypair, text)))
		if ("y" in input("do you have more to encrypt or decrypt? ")):
			userloop_structure()
		else:
			print("Alright, have a nice day!")
	else:
		text = input("What is the text you would like to decrypt: ")
		if "[" in text:
			text = text.replace("[", "")
			text = text.replace("]", "")
			text = text.replace(" ", "")
			text = text.split(",")
			texted = []
			for i in text:
				texted.append(int(i))
			uncipher = RSAdemo.decryptRSA(personalKeypair, texted)
			strUncipher = ""
			for i in uncipher:
				strUncipher += str(i)
			print("The decrypted text is: " + strUncipher)
			if ("y" in input("do you have more to encrypt or decrypt? ")):
				userloop_structure()
			else:
				print("Alright, have a nice day!")
		else:
			print("The inputted text was not a list, and therefore cannot be decrypted")
			userloop_structure()
