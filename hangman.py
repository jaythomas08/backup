# Jarrett Thomas
# Period 4
# October 21st, 2019
# Hangman project

print("Hello, and welcome to hangman!")
numMisses = int(input("please type in number of misses you are allowed: "))

secretWord = list("verrado")
guessList = list("_______")

guessList=[]
for a in secretWord:
	guessList.append("_")
print(guessList)

guess = input("guess a letter: ")
index = 0
for letter in secretWord:
	if letter == guess:
		guessList[index] = guess
	index += 1 
print(guessList)

index = 0
misses = 0
while misses < numMisses:
	guess = input("enter a letter: ")
	if guess in secretWord:
		guessList[index] = guess
	else:
		misses += 1
print(misses)

count = 0
for l in secretWord:
	if l == letter:
		print(count)
		count += 1 

