# Jarrett Thomas
# Period 4
# October 21st, 2019
# Hangman project

import random
myWord = "random"

myString = "myWord"
myList = list(myString )

guessList=[]
for a in myList:
	guessList.append("_")
print(guessList)

letter = input("type a letter") 

if letter in myWord:
	print("letter is in word")
else:
	print("letter is not in word")




count = 0
for l in myWord:
	if l == letter:
		print(count)
		count += 1 