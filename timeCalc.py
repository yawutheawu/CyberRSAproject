import RSAdemo
import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import make_interp_spline, BSpline
import randomBruteForce
import Messages as m1
import time

#https://pynative.com/python-get-execution-time-of-program/
#after getting the execution time for a few different sized keys,
#best fit a curve and then store the equation to estimate future times
rangeDict = {}


def addTo(Key, Value):
	rangeDict[str(Key)] = Value


def test(x, a, b):
	return a * np.exp(b * x)


def estimate():
	print("Starting Estimations")

	startLow = time.time()
	keyPair = RSAdemo.generateKeys(250, 258)
	public_key = keyPair[0]
	private_key = keyPair[1]
	message = "030-88-62**"
	encrypted = RSAdemo.encryptRSA(public_key, message)
	decrypted = RSAdemo.decryptRSA(private_key, encrypted)
	str_dec = ""
	for i in decrypted:
		str_dec += i
	encrypted = RSAdemo.encryptRSA(public_key, message)
	decrypted = RSAdemo.decryptRSA(private_key, encrypted)
	endLow = time.time()
	LowTax = endLow - startLow
	rangeDict[str(251 * 257)] = LowTax

	startMid = time.time()
	keyPair = RSAdemo.generateKeys(500, 510)
	public_key = keyPair[0]
	private_key = keyPair[1]
	message = "030-88-62**"
	encrypted = RSAdemo.encryptRSA(public_key, message)
	decrypted = RSAdemo.decryptRSA(private_key, encrypted)
	str_dec = ""
	for i in decrypted:
		str_dec += i
	encrypted = RSAdemo.encryptRSA(public_key, message)
	decrypted = RSAdemo.decryptRSA(private_key, encrypted)
	endMid = time.time()
	MidTax = endMid - startMid
	rangeDict[str(503 * 509)] = MidTax

	startHigh = time.time()
	keyPair = RSAdemo.generateKeys(1000, 1015)
	public_key = keyPair[0]
	private_key = keyPair[1]
	message = "030-88-62**"
	encrypted = RSAdemo.encryptRSA(public_key, message)
	decrypted = RSAdemo.decryptRSA(private_key, encrypted)
	str_dec = ""
	for i in decrypted:
		str_dec += i
	encrypted = RSAdemo.encryptRSA(public_key, message)
	decrypted = RSAdemo.decryptRSA(private_key, encrypted)
	endHigh = time.time()
	HighTax = endHigh - startHigh
	rangeDict[str(1009 * 1013)] = HighTax

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
	array = x
	equation = []
	for i in array:
		equation.append(3.45 * (1.334**array) + np.random.normal(size=len(array)))
	param, param_cov = curve_fit(test, array, equation)
	ans = (param[0] * (np.exp(param[1] * x)))
	plt.ylabel('Time (seconds)')
	plt.xlabel("N value (p * q)")
	plt.xticks(x)
	plt.plot(array, y, 'o', color='red', label="data")
	plt.plot(array, ans, '--', color='blue', label="optimized data")
	plt.legend()
	plt.show()
