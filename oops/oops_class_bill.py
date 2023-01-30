class bill:
	def __init__(self,Product,Quantity,Price):
		self.Product=Product
		self.Quantity=Quantity
		self.Price=Price
	def show(self):
		print("Product",self.Product)
		print("Quantity",self.Quantity)
		print("Price",self.Price)
s1=bill("Apple","3","150")
s1.show()

