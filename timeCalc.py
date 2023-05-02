import RSAdemo
import matplotlib.pylab as plt
import randomBruteForce
import Messages as m1
import time

#https://pynative.com/python-get-execution-time-of-program/
#after getting the execution time for a few different sized keys,
#best fit a curve and then store the equation to estimate future times
rangeDict = {}
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
MidTax = endMid-startMid
rangeDict[str(503*509)] = MidTax

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
HighTax = endHigh-startHigh
rangeDict[str(1009*1013)] = HighTax

print(rangeDict)
x = list(rangeDict.keys())
temp = []
for i in x:
	temp.append(int(i))
x = temp
y = list(rangeDict.values())
plt.plot(x, y, color='blue', marker='o', linewidth=2, markersize=12)
plt.ylabel('Time (seconds)')
plt.xlabel("N value (p * q)")
plt.xticks(range(min(x) - 1, max(x) + 1))
plt.yticks(range(min(y) - 1, max(y) + 1))
plt.show()
