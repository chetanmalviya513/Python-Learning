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

	def dwrite(self):
		f=open("Employee.txt","a")
		data=self.emp_id + "," + self.name + "," + self.contact + "," + self.address+ "," + self.department +"\n" 
		f.write(data)
		print("data entered sucessfully ")

class manager(employee):
	#employee().__init__()

	def dept_emp_detail(self):
		f=open("Employee.txt","r")
		data = f.read()
		data_row=data.split("\n")
		data_row.pop()
		valid_row=data.split("\n")
		data_row.pop()
		valid_row=[]
		for i in data_row :
			x=i.split(",")
			if self.department==x[len(x)-1]:
				valid_row.append(i)


class owner (manager,employee):
	def show_all(self):
		f=open("employee.txt","r")
		data=f.read()
		data_row=data.split("\n")
		data_row.pop()
		for i in data_row:
			x=i.split(",")
			print("------------")
			print("Employee ID : ",x[0])
			print("Name : ",x[1])
			print("contact : ",x[2])
			print("Address : ",x[3])
			print("Department : ",[4])

s1=employee()
s2=manager()
s3=owner()

s1.dwrite()
s2.dwrite()
s3.dwrite()

s1.show_detail()
s2.show_detail()
s2.dept_emp_detail()
s3.show_detail()
s3.dept_emp_detail()
s3.show_all()






