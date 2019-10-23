print("Welcome to To Do List")
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Choose: ")
	if choice == "q":
		break
	elif choice == "a":
		add = input("What do you want to add? ")
		todoList.append(add)
	elif choice == "r":
		print(todoList)
		remove = input("What would you like to remove? ")
		todoList.remove(remove)
	elif choice == "p":
		print(todoList)
	else:
		print("You chose something not listed")