# Jarrett Thomas
# Period 4
# October 21st, 2019
# Hangman project

secretWord = "arizona cardinals"
secretWord = list(secretWord)

guessList=[]
for a in secretWord:
	guessList.append("_")
print(guessList)

numMisses = int(input("please type in number of misses you are allowed: "))


misses = 0
while misses < numMisses:
	guess = input("enter a letter: ")
	if guess in secretWord:
		print("letter is in word")
	else:
		misses += 1
print(misses)



print("GAME OVER BRUV BETTER LUCK NEXT TIME")