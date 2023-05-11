import RSAdemo
import matplotlib.pylab as plt
import randomBruteForce
import numpy as np

#https://pynative.com/python-get-execution-time-of-program/
#after getting the execution time for a few different sized keys,
#best fit a curve and then store the equation to estimate future times
rangeDict = {}
hackDict = {}


def addTo(Key, Value):
	rangeDict[str(Key)] = Value


def addToHack(Key, Value):
	hackDict[str(Key)] = Value


def test(x, a, b):
	return a * np.exp(b * x)


def estimate(text):
	print("Starting Estimations")

	RSAdemo.forReps(250, 258)
	RSAdemo.forReps(502, 510)
	RSAdemo.forReps(1008, 1014)
	RSAdemo.forReps(1000, 1200)
	RSAdemo.forReps(750, 1000)
	RSAdemo.forReps(500, 750)
	RSAdemo.forReps(350, 500)
	RSAdemo.forReps(100, 350)

	x = list(rangeDict.keys())
	temp = []
	for i in x:
		temp.append(int(i))
	x = temp
	x.sort(reverse=True)
	y = []
	for i in x:
		y.append(int(rangeDict[str(i)]))
	#https://www.geeksforgeeks.org/scipy-curve-fitting/
	plt.ylabel('Time (seconds)')
	plt.xlabel("N value (p * q)")
	plt.title('N size v.s. time to encrypt and decrypt', fontsize=14)
	plt.xticks(x)
	plt.plot(x, y, '-o', color='blue', linewidth=2, label="data")
	plt.grid(True)
	plt.legend()
	plt.show()


def fellasBeHacking(text="testing"):
	print("Hackathon")
	randomBruteForce.primeTimer(text, 0, 150)
	randomBruteForce.primeTimer(text, 150, 250)
	randomBruteForce.primeTimer(text, 250, 350)
	randomBruteForce.primeTimer(text, 350, 450)
	randomBruteForce.primeTimer(text, 450, 550)
	randomBruteForce.primeTimer(text, 550, 650)
	randomBruteForce.primeTimer(text, 650, 750)
	x = list(hackDict.keys())
	temp = []
	for i in x:
		temp.append(int(i))
	x = temp
	x.sort(reverse=True)
	y = []
	for i in x:
		y.append(int(hackDict[str(i)]))
	#https://www.geeksforgeeks.org/scipy-curve-fitting/
	plt.ylabel('Time (seconds)')
	plt.xlabel("N value (p * q)")
	plt.title('N size v.s. time to brute force factorize', fontsize=14)
	plt.xticks(x)
	plt.plot(x,
	         y,
	         '-o',
	         color='blue',
	         linewidth=2,
	         label=f"Brute force message used: {text}")
	plt.grid(True)
	plt.legend()
	plt.show()
