"""def myfunction():
		x=int(input("Enter value : "))
		y=int(input("Enter value : "))
		z=x+y
		#print(z)
		print(i)
	
	i="I am outside"
	myfunction()
	#print(z)
	"""	
"""def myfunction():
		x=int(input("Enter value : "))
		y=int(input("Enter value : "))
		z=x+y
		print(z)
		i="I am inside"
	
	i="I am fine "
	print(i)
	myfunction()
	print(i)
	"""	
"""def myfunction():
	x=int(input("Enter value : "))
	y=int(input("Enter value : "))
	z=x+y
	print(z)
	i="I am inside"
	print(id(i))

i="I am fine "
print(id(i))
print(i)
myfunction()
print(i)
"""

def myfunction():
	global i 
	x=int(input("Enter value : "))
	y=int(input("Enter value : "))
	z=x+y
	print(z)
	i="I am inside"
	print(id(i))

i="I am fine "
print(id(i))
print(i)
myfunction()
print(i)




