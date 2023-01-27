def takechoice():
	choice = input("Enter y to continue or n to close : ")
	if choice == "y" or choice=="Y":
		return True 
	elif choice == "n" or choice=="N":
		return False
	else : 
		print("Invalid Input")
		takechoice()
