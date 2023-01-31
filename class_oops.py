class Details_all:
	def __init__(self):
		self.name=input("Enter Name : ")
		self.course=input("Enter Course : ")
		self.college=input("Enter College : ")
		self.Address=input("Enter Address : ")
		self.contact=input("Enter contact : ")
	def show(self):
			print("Name : ",self.name)
			print("Course : ",self.course)
			print("college",self.college)
			print("Address",self.Address)
			print("contact",self.contact)
s1=Details_all()
s1.show()