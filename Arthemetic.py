def calc():
	var1=int(input("Enter value 1 "))
	var2=int(input("Enter value 2 "))
	choice=input("Enter 1 for add\n 1 for sub \n 3 for mul \n 4 for Div \n")

	if choice == "1":
		result=var1+var2
		print("Result",result)
	elif choice == "2":
		result = var1 - var2
		print(result)
	elif choice == "3":
		result = var1 * var2 
		print(result)
	elif choice == "4":
		result = var1/var2
		print(result)
	else : 
		print("invalid operation given")
		calc()
		