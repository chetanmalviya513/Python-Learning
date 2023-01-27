"""

p=int(input("price"))
d=int(input("discount"))
c=int(input("cgst"))
s=int(input("sgst"))
t=p-d+c+s
print("total",t)    

"""

p=14
b=22
m=15
m,b=11
b,p=8
m,p=5
m,p,b=3

t=p+b+m-m,b-b,p-m,p+m,b,p
print(t)