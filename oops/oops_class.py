class student:
	def __init__(self,name,course,subject):
		self.name=name
		self.course=course
		self.subject=subject
	def show(self):
		print("Name :",self.name)
		print("course",self.course)
		print("subject",self.subject)

s1=student("Rahul","Msc","Maths")
s1.show()