myWord = "Hello"

choice = input("Type a word: ")
if choice == myWord:
	print("It's a match")
else:
	print("Not a match")


#How to check if a letter is in a word

letter = input("Enter a letter: ")

if letter in myWord:
		print("That letter is in myWord")
else:
	print("That letter is not in word")

count = 0
for letter2 in myWord:
	if letter2 == letter:
		print (count)
	count += 1








