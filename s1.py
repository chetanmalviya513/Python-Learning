"""
s1="noon"
s2="noon"
if s1==s2:
	print("eual")
else:
	print("not equal")

"""
#strip function is use to remove white space in string
"""
s1="noon"
s2="noon "
s1=s2.strip()
s2=s2.strip()
if s1==s2:
	print("eual")
else:
	print("not equal")

"""

#reverse the string
"""
userstr=input("Enter your string:")
reverse=""
for i in range(len(userstr)-1,-1,-1):
	reverse=reverse+userstr[i]
print("user given is {}".format(userstr))
print("Reverse string is{}".format(reverse))

"""
"""
userstr=input("Enter your string:")
reverse=userstr[::-1]
print("userstr=",userstr)
print("reverse=",reverse)
"""
"""
list1=[15,12,12,5,45,56]
list1.append(23)
print(list1)
print(id(list1))
list1.remove(15)
print(list1)
print(id(list1))
"""
"""
l1=[1,2,3,4,5,6,7]
l2=[8,9,10,11]
#print(l1,l2)
l1=l1+l2
#print(l1,l2)
l3=[12,13,14,15,]
l1=l1+l3
l1.append(l2)
print(l1)

"""
