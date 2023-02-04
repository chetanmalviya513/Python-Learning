"""Amount=0
unit=int(input("Enter unit : "))
if unit<=100:
	Amount=0
if unit>100 and unit<=200:
	Amount=(unit-100)*5
if unit>200:
	Amount=500+(unit-200)*10
print("Amount t o pay : ",Amount)	

"""
"""num=int(input("Enter any number "))
print("Last digit of number is ",num%10)"""

num=int(input("Enter any number : "))
Id=num%10
if Id%3==0:
	print("Last digit of number is divisible by 3 ")
else:
	print("Last digit of number is not divisible by 3 ")