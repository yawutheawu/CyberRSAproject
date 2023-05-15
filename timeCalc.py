import RSAdemo
import matplotlib.pylab as plt
import randomBruteForce
import json
import numpy as np

#https://pynative.com/python-get-execution-time-of-program/
#after getting the execution time for a few different sized keys,
#best fit a curve and then store the equation to estimate future times (did not do this just making curves to show the exponential increase in time)
rangeDict = {}
hackDict = {}


def setHack(dict):
	hackDict = dict


def setRange(dict):
	rangeDict = dict


def addTo(Key, Value):
	rangeDict[str(Key)] = Value
	with open("rangeDict.json", "w") as f:
		json.dump(rangeDict, f)


def addToHack(Key, Value):
	hackDict[str(Key)] = Value
	with open("hackDict.json", "w") as f:
		json.dump(hackDict, f)


def test(x, a, b):
	return a * np.exp(b * x)


def estimate(text):
	print("Starting Estimations")
	for i in range(100, 1500, 100):
		RSAdemo.forReps(i, i + 150)
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
	for i in range(100, 1500, 100):
		randomBruteForce.primeTimer(text, i, i + 150)
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
