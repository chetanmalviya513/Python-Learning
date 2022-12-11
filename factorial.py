"""
i=int(input("Enter fact:"))
fact=1
if i==0 or i==1:
	print("{} is factorial of {}".format(fact,i))
else:
	for j in range(1,i+1):
		fact=fact*j
print("{} is factorial of {}".format(fact,i))
"""
x=int(input("Enter no:"))
fact=1
for i in range(x,0,-1):
	fact=fact*i
print("factorial of {}={}".format(x,fact))

