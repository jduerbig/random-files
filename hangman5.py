#how to replace underscores with letters

mystery = "halloween"
mystery = list(mystery)

guessList = "_______"
guessList = list(guessList)

guess = input("Guess a Letter")

if guess in mystery:
	count = 0
	for letter in mystery:
		if letter == guess:
			guessList[count] = guess
		count += 1

print(guessList)