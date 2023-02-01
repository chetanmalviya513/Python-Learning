"""num=int(input("Enter Num : "))
f=1
for i in range(1,num+1):
	f=f*i
print("Factorial Number : ",f)"""

"""num=int(input("Enter Num : "))
f=1
for i in range(1,num+1):
	f=f*i
print("Factorial")
"""
"""num=int(input("Enter any number : "))
s=0
while(num):
	r=num%10
	s=s+r
	num=num//10
print("Sum of digits is ",s)"""

num=int(input("Enter any number"))
f=0
if num==1 or num==0:
	f=1
for i in range(2,num):
	if num%i==0:
		f=1
if f==1:
	print("number is not prime")
else:
	print("number is prime")