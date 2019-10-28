import random
import os
import time



while True:
	words = ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt",
 	"sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo"
	]
	myString = random.choice(words)
	secretWord = list(myString)
	print(secretWord)
	guessList = []
	errors = 0

	for letter in secretWord:
		guessList.append("_")





	HANGMAN = [ 


 '''
   +----+
        |
        |
        |
        |
        |
  =========
  ''',
  '''
   +----+
   o    |
        |
        |
        |
        |
  =========
   ''',
   '''
   +----+
   o    |
   |    |
        |
        |
        |
  =========
    ''',
    '''
   +----+
   o    |
   |\   |
        |
        |
        |
  =========
     ''',
     '''
   +----+
   o    |
  /|\   |
        |
        |
        |
  =========
      ''',
      '''
   +----+
   o    |
  /|\   |
  /     |
        |
        |
  =========
       ''',
       '''
   +----+
   o    |
  /|\   |
  / \   |
        |
        |
  =========
        '''
        ]



	print(HANGMAN[0])
	attempts = len(HANGMAN) - 1



	while True:
		guess = input("guess a letter A-Z ")
		if guess in secretWord:
			print("That letter is in the word")
			count = 0
			for letter in secretWord:
				if letter == guess:
					guessList[count] = guess
				count += 1
			print(guessList)

		else:
			print("That letter is not in the word")
			attempts -= 1
			print(HANGMAN[(len(HANGMAN) - 1) - attempts])





























