"""
raining=input("it is raining? ")
raining=str.lower(raining)
if raining=="yes":
	windy=input("it is windy?")
	windy=str.lower(windy)
	if windy=="yes":
		print("it is too windy for an umbrella")
	else:
		print("take an umbrella")
else:
	print("Enjoy your day")
"""

course=input("Enter your course")
course=str.lower(course)

if course=="pg":
	program=input("Enter your pg program")
	program=str.upper(program)
	if program=="MBA" or program=="MCA" or program=="MSC" or program=="MTEC" or program=="MCOM":
		print("post graguation")
	else:
		print("invalid program")
elif course=="ug":
	program=input("Enter your ug program")
	program=str.upper(program)
	if program=="BBA" or program=="BSC" or program=="BTEC" or program=="BCA" or program=="BCOM": 
		print("under graguation")
	else:
		print("invalid program")
else:
	print("other program")



