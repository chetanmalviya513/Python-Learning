"""n=int(input("Enter value:"))
for i in range(0,n):
	for j in range(0,i+1):
		print("*",end="")
	print("\r")"""

"""n=int(input("Enter value:"))
list1 = []
value = ""
for i in range(1,n+1):
	for j in range(1,n+1):
		if j <= n-i :
			value = value + " "
		else :
			for k in range()


	list1.append(value)
	value = ""

for i in list1 :
	print(i)"""

n=int(input("Enter value:"))
list1 = []
value = ""
for i in range(1,n+1):
	for j in range(1,i+1):
		value = value + str(j)
	if len(value) < n :
		sub = n-len(value)
		value = (sub * " ")+ value 
	#value = value[::-1]		
	list1.append(value)
	value = ""

for i in list1 :
	print(i)


