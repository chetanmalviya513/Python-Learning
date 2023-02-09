roll_no = 0
class student:
	def __init__(self):
		self.name=(input("Enter student's name : "))
		self.fathername=input("Enter student's father;s name : ")
		self.age=input("Enter Age : ")
		self.year=input("Enter year : ")
		self.course=input("Enter course : ")
		self.contact=input("Enter contact : ")

	def show_detail(self):
		print("Name : ",self.name)
		print("father's Name : ",self.fathername)
		print("Age : ",self.age)
		print("year of joining : ",self.year)
		print("course : ",self.course)
		print("contact Detail : ",self.contact)

	def generate_rollno(self):
		global roll_no
		roll_no = roll_no+1
		self.roll_no=roll_no
		print("Roll no. of student : ",self.roll_no)

print(roll_no)		
s1=student()
s1.generate_rollno()
s1.show_detail()
print(roll_no)