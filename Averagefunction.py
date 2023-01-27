"""
def average(x,y,z):
	avg=(x+y+z)/3
	return avg
a=int(input("Enter First:"))
b=int(input("Enter second:"))
c=int(input("Enter third:"))
d=average(a,b,c)
print(a,b,c,d)
"""
#Average all value accept

choice=int(input("Enter no. of term:"))
sum=0
for i in range (choice):
	value=int(input("Enter value:"))
	sum=sum+value
Average=sum/choice
print("Average",Average)
