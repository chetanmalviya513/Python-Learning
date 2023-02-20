"""class student:
	def __init__(self,name,course,subject):
		self.name=name
		self.course=course
		self.subject=subject
	def show(self):
		print("Name:",self.name)
		print("course:",self.course)
		print("subject:",self.subject)
s1=student("Lokesh","Mca","Python")
s1.show()
"""
class student:
	def __init__(self):
		self.name=input("Enter Name : ")
		self.course=input("Enter Course : ")
		self.subject=input("Enter Subject : ")
	def show(self):
		print("Name:",self.name)
		print("course:",self.course)
		print("subject:",self.subject)
s1=student()
s1.show()
s2=student()
s2.show()