a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
d=int(input("d"))
e=int(input("e"))
smallest=0

list=a,b,c,d,e,smallest
print(list) 
if (smallest>a):
	smallest,a=a,smallest 
if (smallest>b):
	smallest,b=b,smallest
if (smallest>c):
	smallest,c=c,smallest
if (smallest>d):
	smallest,d=d,smallest
if (smallest>e):
	smallest,e=e,smallest

print(smallest)




