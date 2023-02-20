class employee:
	def __init__(self):
		self.name=input("Enter name of employee : ")
		self.emp_id=input("Enter employee id : ")
		self.contact=input("Enter contact number of employee : ")
		self.address=input("Enter address of employee : ")
		self.department=input("Enter Department : ")

	def show_detail(self):
		print("Employee ID : ",self.emp_id)
		print("Name : ",self.name)
		print("contact : ",self.contact)
		print("Address : ",self.address)

	def write(self):
		f=open("Employee.txt","a")
		data=self.emp_id + "\n" + self.name + "\n" + self.contact + "\n" + self.address+ "\n" + self.department +"\n" 
		f.write(data)
		print("data entered sucessfully ")

class manager(employee):
	#employee().__init__()

	def dept_emp_detail(self):
		f=open("Employee","r")
		data = f.read()
		data_row=data.splite("\n")
		data_row.pop()
		valid_row=data.splite("\n")
		data_row.pop()
		valid_row=[]
		for i in data_row :
			x=i.splite(",")
			if self.dept==x[len(x)-1]:
				valid_row.append(i)	





