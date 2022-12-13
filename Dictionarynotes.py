#Dictionary
#
"""
dict1={"Name":"Deepak","class":"Bca","subject":"coomerce"}
print(dict1)
"""
"""
dict1={"Name":"Deepak","class":"Bca","subject":"coomerce"}
for i in dict1:
	print(i)
	print(dict1[i])
	"""
"""
dict2={1:"23",2:"25",3:"26",3:"26"}
for i ,j in dict2.items():
print(i)
print(j)
"""

dict1={"Name":"Deepak","class":"Bca","subject":"coomerce"}
for i,j in dict1.items():
	print(i)
	print(j)

dict1["noon"]="sunny"
print(dict1)
dict1["school"]="nhi pata"
print(dict1)
dict1.pop("Name")
print(dict1)