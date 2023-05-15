import json
import timeCalc

with open("rangeDict.json", "r") as f:
	rangeDict = json.load(f)
with open("tempRange.json", "r") as f:
	tempRange = json.load(f)
with open("tempHack.json", "r") as f:
	tempHack = json.load(f)
with open("hackDict.json", "r") as f:
	hackDict = json.load(f)

newRange = {}
for i in list(rangeDict.keys()):
	newRange[i] = rangeDict[i]
for i in list(list(tempRange.keys())):
	newRange[i] = tempRange[i]
newHack = {}

for i in list(hackDict.keys()):
	newHack[i] = hackDict[i]
for i in list(list(tempHack.keys())):
	newHack[i] = tempHack[i]

timeCalc.setHack(newHack)
timeCalc.setRange(newRange)

empty = {}

with open("tempHack.json", "w") as f:
	json.dump(empty, f)
with open("tempRange.json", "w") as f:
	json.dump(empty, f)
