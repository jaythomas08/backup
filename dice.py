# Name: Jarrett Thomas 
# Period: 4th
# Date: Oct 2nd, 2019
# Dice Rolling Simulator

import random

rollNumber = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0


print()


print ("Welcome to the Dice Rolling Simulator!")


print()


playerChoice = int(input("How many times would you like to roll the dice? "))

print()


while True:
	rollNumber = rollNumber + 1
	randomNum = random.randint(1,6)
	print ("Roll number: " + str(rollNumber) + "  " + "What the dice landed on: " + str(randomNum))
	if rollNumber >= playerChoice:
		if randomNum == 1:
			ones = ones + 1
		elif randomNum == 2:
			twos = twos + 1
		elif randomNum == 3:
			threes = threes + 1
		elif randomNum == 4:
			fours = fours + 1
		elif randomNum == 5:
			fives = fives + 1
		elif randomNum == 6:
			sixes = sixes + 1
		break

	elif randomNum == 1:
		ones = ones + 1
	elif randomNum == 2:
		twos = twos + 1
	elif randomNum == 3:
		threes = threes + 1
	elif randomNum == 4:
		fours = fours + 1
	elif randomNum == 5:
		fives = fives + 1
	elif randomNum == 6:
		sixes = sixes + 1


print()


print ("Results after rolling the dice " + str(playerChoice) + " times: ")


print()


print ("Times it landed on one: " + str(ones))
print ("Times it landed on two: " + str(twos))
print ("Times it landed on three: " + str(threes))
print ("Times it landed on four: " + str(fours))
print ("Times it landed on five: " + str(fives))
print ("Times it landed on six: " + str(sixes))


print()


print ("Percentage of rolls that landed on one: " + str(((ones) / (rollNumber))*100) + " " + "%")
print ("Percentage of rolls that landed on two: " + str(((twos) / (rollNumber))*100) + " " + "%")
print ("Percenatge of rolls that landed on three: " + str(((threes) / (rollNumber))*100) + " " + "%")
print ("Percentage of rolls that landed on four: " + str(((fours) / (rollNumber))*100) + " " + "%")
print ("Percetange of rolls that landed on five: " + str(((fives) / (rollNumber))*100) + " " + "%")
print ("Percentage of rolls that landed on six: " + str(((sixes) / (rollNumber))*100) + " " + "%")

print()