sum=first_int+second_int+third_int
smallest=first_int
if smallest>second_int:
	smallest=second_int
if smallest>third_int:
	smallest=third_int

best2_int=sum-smallest
print("Best_2_int : ",best2_int)
