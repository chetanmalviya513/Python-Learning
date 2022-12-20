#function
"""
def rect_area():
	length=int(input("Enter length:"))
	Breath=int(input("Enter Breath:"))
	Area=length*Breath
	print("Area of Rectangle =",Area)
rect_area()
rect_area()
rect_area()
rect_area()
"""
# function for loop
"""
def rect_area():
	length=int(input("Enter length:"))
	Breath=int(input("Enter Breath:"))
	Area=length*Breath
	print("Area of Rectangle =",Area)
for i in range(4):
	rect_area()
		
"""
#factorial in function
"""
def factorial(x):
	fact=1
	if x==0 or x==1:
		fact=1
	else:
		for i in range(1,x+1):
			fact=fact*i
	return fact
for i in range(4):
	choice=int(input("Enter value:"))
	factorial_value=factorial(choice)
	print("factorial of {} is {} ".format(choice,factorial_value))
"""

#Average Dificult &  

def average(x,y,z):
	avg=(x+y+z)/3
	return avg
a=int(input("Enter first:"))
b=int(input("Enter second:"))
c=int(input("Enter third:"))
d=average(a,b,c)
print(a,b,c,d)


#Average All value function
"""
choice=int(input("Enter no. of term:"))
sum=0
for i in range(choice):
	value=int(input("Enter value:"))
	sum=sum+value
Average=sum/choice
print("Average",Average)
"""