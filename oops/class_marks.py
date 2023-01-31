class marks:
	def __init__(self,name,course,subject,marks):
		self.name=name
		self.course=course
		self.subject=subject
		self.marks=marks
	def show (self):
		print("Name : ",self.name)
		print("course : ",self.course)
		print("Subject : ",self.subject)
		print("marks : ",self.marks)

s1=marks("Lucky","Mba","Qt","55")
s1.show()