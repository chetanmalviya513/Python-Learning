#step:1 Enter Details of student
def mark_int():
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
mark_int()


