x=int(input("enter first number = "))
y=int(input("enter second number ="))
z=int(input("enter third number = "))

print(type(x))
print(type(y))
print(type(z))
if x>=y and x>=z:
	print(x," is greater")
elif (y>=x and y>=z) :
	print(y," is greatest")
else:
	print(z," is greatest")