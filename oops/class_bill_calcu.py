class bill:
	def __init__(self):
		self.product=input("Enter Product : ")
		self.quantity=int(input("Enter Quantity : "))
		self.price=int(input("Enter price : "))		
		self.total=int(input("Enter total : "))
	def show(self):
		print("product",self.product)
		print("quantity",self.quantity)
		print("price",self.price)
		print("Total",self.total)
s1=bill()
s1.show()