# John Duerbig


#break into pieces
#welcome page, with name entry
# score screen with computer, player (name), ties
# options for game r, p, s, q
#game will loop untill q is entered
#each loop it will get a random choice from the computer
#a choice from the player, compare the two, and update the score
# when the game is over (q is entered) final score is displayed

# welcome page
# prompt for name
# a welcome message
#_________________________________________________________________

# imports
import random
# variables
playerScore = 0
computerScore= 0
ties = 0
#make a list
cChoices =["r", "p", "s"]



print("Welcome to Rock Paper Scissors")
name = input("Enter your name")
#main loop
while True:
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to quit: ")
	computerChoice = random.choice(cChoices)
	print(computerChoice)
	if choice == "q":
		break
	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r": # Tie
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1
	elif choice == "p":
		print(name + " Picked Paper")
		if computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		if computerChoice == "r":
			print("Computer picked Rock")
			print("Paper beats Rock")
			playerScore += 1
		if computerChoice == "s":
			print("Computer picked Scissors")
			print("Scissors beats Paper")
			computerScore += 1
	elif choice == "s":
		print(name + " Picked Scissors")
		if computerChoice == "s":
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
		if computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1
		if computerChoice == "p":
			print("Computer picked Paper")
			print("Scissors beats Paper")
			playerScore += 1
	else:
		print("Not an option, try again")



