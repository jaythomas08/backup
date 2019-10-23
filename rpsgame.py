# Jarrett Thomas
# Rock Paper Scissors
# added a comment 
# VARIABLES
import random 
pScore = 0 
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]


# Welcome Message
# Print the message 
print("Welcome to Rock Paper Scissors")
# Prompt for the player name
pName= input("What is your name? ")

# final score
def printScore():
	# write message
	print("the score is: ")
# write player score
	print(pName + ":" + str(pScore))
# write computer score
	print("Computer: " + str(cScore))
# write how many ties 
	print("Ties: " + str(ties))

# Game loop
# make a forever loop
while True:
	# print current score
	printScore()
	# prompt for a choice (r (rock), p (paper), s (scissors), q(quit))
	pChoice = input("Enter r (rock), p (paper), s (scissors), q (to quit): ")
	# deal with player entering q
	if pChoice == "q":
		break
	# get computers choice (random)	
	cChoice = random.choice("computerChoices")
	# compare for player entering r
	if pChoice == "r":
		print(pName + "picked rock")
		#if computer is r
		if cChoice == "r":
			print("computer picked rock")
			print("this is a tie")
			ties = ties + 1
		# if computer is p
		elif cChoice == "P":
			print("computer picked paper")
			print("paper covers rock")
			cScore = cScore + 1
		# if computer is s 
		else:
			print("computer picked scissors")
			print("rock breaks scissors")
			pScore = pScore + 1 

	# compare for player entering p
	elif pChoice == "p":
		print(pName + "picked paper")
		if cChoice == "r":
			print("computer picked rock")
			print("paper covers rock")
			pScore = pScore + 1
		elif cChoice == "p":
			print("computer picked paper")
			print("this is a tie")
			ties = ties + 1 
		else:
			print("computer picked scissors")
			print("scissors cut paper")
			cScore = cScore + 1 
	
	# compare for player entering s 
	elif pChoice == "s":
		print(pName + "picked scissors")
		if cChoice == "r":
			print("computer picked rock")
			print("rock breaks scissors")
			cScore = cScore + 1
		elif cChoice == "p":
			print("computer picked paper")
			print("scissors cut paper")
			pScore =pScore + 1 
		else:
			print("computer picked scissors")
			print("this is a tie")
			ties = ties  + 1 

	# deal with player entering anything else
