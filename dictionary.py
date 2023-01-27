"""
var1={"Name":"Ank
it","Class":"M.tec","College":"Sods"}
print(var1)

for i in var1:
	print(i)
	print(var1[i])

for i,j in var1.items():
	print(i)
	print(j)

var1["Address"]="Mari mata"
var1.pop("College")
print(var1)

"""

Name1=input(" Enter 1 ")
Class2=input(" Enter 2 ")
College3=input(" Enter 3 ")

Details=Name1+Class2+College3
#print(Details)

for i in Details:
	print(Details)
	