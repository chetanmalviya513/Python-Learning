def driving_licence():
	age=int(input("Enter your age "))
	if age>=18:
		print("Eligible for license ")
	elif age>=16:
		print("Eligible for Scuty license ")
	else:
		print("Not Eligible ")
for i in range(1,5):
	driving_licence()



