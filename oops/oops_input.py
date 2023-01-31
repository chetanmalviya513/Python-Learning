class bill_details:
	def __init__(self):
		self.product=input("Enter Product : ")
		self.price=int(input("Enter Price : "))
		self.Quantity=int(input("Enter address : "))
		self.Total=int(input("Enter Total : "))
	def show (self):
		print("product : ",self.product)
		print("price : ",self.price)
		print("Quantity : ",self.Quantity)
		print("Total : ",self.Total)
s1=bill_details()
s1.show()
