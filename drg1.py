# John Duerbig
# period 1
# 10/2/2019
import random
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
RN = 1

die = input("Enter how many times that the dice will roll")
die = int
while RN <= int(die):
	RandNum = random.randint(1,6)
	print("Roll Number",RN,":", RandNum)
	RN += 1
	if RandNum == "1":
		ones += 1
	if RandNum == "2":
		twos += 1
	if RandNum == "3":
		threes += 1
	if RandNum == "4":
		fours += 1
	if RandNum == "5":
		fives += 1
	if RandNum == "6":
		sixes += 1

print(ones)

	


