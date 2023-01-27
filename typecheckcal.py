
a=input("Enter first value:")
b=input("Enter second value:")

def type_check(x):
	 num_char=["0,","1","2","3","4","5","6","7","8","9"]
	 num_count=0
	 dot_count=0

	 for i in x:
	 	if i in num_char:
	 		num_count+=1

	 	else:
	 		dot_count+=1

	 if num_count==1 and dot_count==0:
	 	x=int(x)
	 else:
	 	x=float(x)

	 return x

def calculator(n):
	if n==1:
		add = return_value1+return_value2

		print("Addition of {} and {} is {}".format(return_value1,return_value2,add))
		return add
	elif n==2:
		a=input("Enter first value:")
		b=input("Enter second value:")
		sub = return_value1- return_value2
		print("Subtraction of {} and {} is {}".format(a,b,add))
		return sub

	elif n==3:
		a=input("Enter first value:")
		b=input("Enter second value:")
		mul = a*b
		print("Multiplication of {} and {} is {}".format(a,b,))
		return mul

	elif n==4:
		a=input("Enter first value:")
		b=input("Enter second value:")
		div = a/b
		print("Division of {} and {} is {}".format(a,b,add))
		return div

	else:
		print("Wrong Choice...!")

	choice =int(input("Enter choice: ")) 
	calculator(choice)
return_value1=type_check(a)
return_value2=type_check(a)
print("type of a:", type(return_value1))
print("type of b:", type(return_value2))

"""
x=int(input("Enter no:"))
fact=1
for i in range(x,0,-1):
	fact=fact*i
print("factorial of {}={}".format(x,fact))
"""
































