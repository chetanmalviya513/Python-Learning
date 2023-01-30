class student:
	def __init__(self):
		self.name=input("Enter Name : ")
		self.course=input("Enter course : ")
		self.subject=input("Enter subject : ")
	def show(self):
		print("Name :",self.name)
		print("course",self.course)
		print("subject",self.subject)

s1=student()
s1.show()
s2=student()
s2.show()