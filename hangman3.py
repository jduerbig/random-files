import random
import os
import time

words = ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt",
 "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo"
]
myString = random.choice(words)
secretWord = list(myString)
print(secretWord)
guessList = []

for letter in secretWord:
	guessList.append("_")


frame1 = [
'''
   +----+
        |
        |
        |
        |
        |
  =========
  '''      


]

for frame in frame1:
	print(frame)
	os.system("cls")



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



while True:
	guess = input("guess a letter A-Z")
	if guess in secretWord:
		print("Letter in word")
	else:
		os.system("cls")
		for frame in HANGMAN:
			print(frame)
			os.system("cls")
			print(guessList)







