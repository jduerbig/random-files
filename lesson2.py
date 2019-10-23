#conditionals

age = input("what is your age?") #prmpt for age

#check if age is more than 17, so that the person can see R movies

age = int(age)
if age > 17: #everything in the "if" statement only tun when the condition is true
	print("you can see an R rated movie")

else:
	print("you cannot see an R rated movie, too bad so sad")

print("have a nice day")
#you can check all these conditions
#>, <, >=, <=, == (== means equal to)

birthday = input("Is today your birthday (yes or no)?")
if birthday == "yes":
	print("happy birthday")

print("have a nice day")

myNum = 7
guess = input("guess a number between 1 and 10?")
guess = int(guess)
if guess == myNum:
	print("You guessed correctly!")
elif guess > myNum:
	print("Too High!")
else:
	print("Too Low")
print("thanks for playing")


