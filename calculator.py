"""
First = int(input("Enter first number"))
Second = int(input("Enter Second number"))
Operator = input("Enter operator (+,-,*,/)")


if Operator	== "+":
	print(First	+ Second)
elif Operator == "-":
	print(First	- Second)
elif Operator == "*":
	print(First	* Second)
elif Operator == "/":
	print(First	/ Second)
else:
	print("Invalid Operation")
"""
"""
def Calculator():
	First = int(input("Enter first number"))
	Second = int(input("Enter Second number"))
	Operator = input("Enter operator (+,-,*,/)")


	if Operator	== "+":
		print(First	+ Second)
	elif Operator == "-":
		print(First	- Second)
	elif Operator == "*":
		print(First	* Second)
	elif Operator == "/":
		print(First	/ Second)
	else:
		print("Invalid Operation")

Calculator()
"""

# Define Function for Addition
def sum():
	First_Num = int(input("Enter 1st Num :"))
	Second_num = int(input("ENter 2nd Num :"))
	Total = First_Num + Second_num
	print(Total)

# Define Function for Subtraction
def sub():
	First_Num = int(input("Enter 1st Num :"))
	Second_num = int(input("ENter 2nd Num :"))
	Total = First_Num - Second_num
	print(Total)

# Define Function for Multiple
def mul():
	First_Num = int(input("Enter 1st Num :"))
	Second_num = int(input("ENter 2nd Num :"))
	Total = First_Num * Second_num
	print(Total)

# Define Function For Division
def div():
	First_Num = int(input("Enter 1st Num :"))
	Second_num = int(input("Enter 2nd Num :"))
	Total = First_Num / Second_num
	print(Total)

# Define Function Floor Division
def Floor_Division():
	First_Num = int(input("Enter 1st Num :"))
	Second_num = int(input("Enter 2nd Num :"))
	Total = First_Num // Second_num
	print(Total)

# Define Function For Reminder
def Reminder():
	First_Num = int(input("Enter 1st Num :"))
	Second_num = int(input("Enter 2nd Num :"))
	Total = First_Num % Second_num
	print(Total)

# Define Function For Interest 
def Int():
	Principle = int(input("Enter Principle :"))
	Rate_of_interest = int(input("Enter Rate :"))
	Time_Year = int(input("Enter Time_Year :"))
	Total = Principle * Rate_of_interest * Time_Year / 100
	print(Total)



# Print intruction
print("Enter Operator")
print("Enter + > Sum of Two Number :")
print("Enter - > sub of Two Number :")
print("Enter * > mul of Two Number :")
print("Enter / > div of Two Number :")
print("Enter // > Floor_Division of Two Number :")
print("Enter % > Reminder of Two Number :")
print("Enter Int > Int Calculate :")

# Perform Operation
Operator = input("Enter Operator :")
if Operator == "+":
	sum()
elif Operator == "-":
	sub()
elif Operator == "*":
	mul()
elif Operator == "/":
	div()
elif Operator == "//":
	Floor_Division()
elif Operator == "%":
	Reminder()
elif Operator == "Int":
	Int()
else:
	print("Invalid Operator")




