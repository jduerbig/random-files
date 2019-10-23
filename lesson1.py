# calculating, printing, variables

# Printing to the screen
# The built in function print(), prints to the screen
# it will print both Strings and numbers
print("printing to the screen...")
print("hello") #a string
print('hello again')
print(6) # a number
print("6") # a string again
print(6+6) #12
print("6"+"6") # string concationation

# perfroming Calculations
# addition +
# subtraction -
# multiplication *
# division /
# exponents **
# modulo %

print (4-2) #->2
print (4*2) #->8
print (4/2) #->2
print (4**3)#->64 
print("modulo operator test")
print(5%3)
print(10%2)
print (16%3)
# modulo gives remainders
# python operators follow the same order of operations as Math
print(4-2*2) #should be 0
print((4-2)*2) #should be 4

# variables
# variables are usde to hold data
# variables are declared and set to a value (initializing)
badluck = 13 # declared a variable called badluck and initialized it to 13
# i can print the variable using it's name
print("badluck = " + str(badluck)) #cast it to a string
# lets do another one
goodluck = "4" # String variable
print("goodluck = " + goodluck) # don't have to cast
badluck + 5 #this is pointless
print(badluck)
badluck = badluck + 5 # now badluck is 18
print(badluck)

# you can also save input into the variables
# using input(), A prompt goes inside the ()
name = input("what is your name?")
print("hello" + name)
print(name * 10)
name = name + "\n" #escape character (newline)
print(name * 10)
# lets try some math
base = input("Enter the base number: ")
exp = input("enter the exponent: ")
print(int(base) ** int(exp))
