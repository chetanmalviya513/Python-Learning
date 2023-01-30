class bill:
	def __init__(self):
		self.product=input("Enter Product : ")
		self.quantity=input("Enter Quantity : ")
		self.price=int(input("Enter price : "))
	def show(self):
		print("product",self.product)
		print("quantity",self.quantity)
		print("price",self.price)
s1=bill()
s1.show()