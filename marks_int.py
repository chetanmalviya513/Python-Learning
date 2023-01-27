#step:1 Enter Details of student
mark_int=open("mark_int.txt","w")
name=input("Enter student name : ")
Roll_no=input("Enter roll_no : ")
first_int=int(input("Enter 1st int : "))
second_int=int(input("Enter 2st int : "))
third_int=int(input("Enter 3st int : "))
details="Name : {} , Roll_no : {} , first_int : {} , second_int : {} , third_int {}".format(name,Roll_no,first_int,second_int,third_int)
mark_int.write(details)
mark_int.close()

#step:2 mark_int read
mark_res=open("mark_int.txt","r")
res=mark_res.read()
print(res)

#step:3 best of 2 internal
sum=first_int+second_int+third_int
smallest=first_int
if smallest>second_int:
	smallest=second_int
if smallest>third_int:
	smallest=third_int

#step:4 Grade of student

best2_int=sum-smallest
print("Best_2_int : ",best2_int)

if best2_int>35:
	print("Grade : ","A")
elif best2_int>30:
	print("Grade : ","B")
elif best2_int>25:
	print("Grade : ","C")
elif best2_int>20:
	print("Grade : ","D")
else:
	print("Grade : ","Fail")