class bill:
	def __init__(self):
		self.product=input("Enter Product : ")
		self.quantity=int(input("Enter Quantity : "))
		self.price=int(input("Enter price : "))
		
	def show(self):
		total=self.quantity*self.price
		print("product",self.product)
		print("quantity",self.quantity)
		print("price",self.price)
		print("total = ",total)
	

	
		
		 
s1=bill()
s1.show()