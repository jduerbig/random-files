import random
import os
import time

words = ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo"
]
myString = random.choice(words)
secretWord = list(myString)
print(secretWord)
guessList = []

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

while True:
	os.system("cls")
	for frame in HANGMAN:
		print(frame)
		time.sleep(.2)
		os.system("cls")

print()





