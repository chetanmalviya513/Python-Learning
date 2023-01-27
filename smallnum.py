a=int(input("Enter num"))
b=int(input("Enter num"))
c=int(input("Enter num"))

sum=a+b+c
smallest=a

if smallest>b:
	smallest=b
if smallest>c:
	smallest=c

bestof_3=sum-smallest
print(bestof_3)

