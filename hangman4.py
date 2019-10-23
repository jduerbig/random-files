secretWord = "Christmas"
secretWord = list(secretWord)
print(secretWord)
misses = 0


guess = imput("Guess A Letter")

if guess in secretWord:
	print("Letter in Word")
else:
	misses = misses + 1

print("misses: " + str(misses))
print(hangman[misses])