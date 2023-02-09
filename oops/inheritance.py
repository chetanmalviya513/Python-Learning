"""class squre:
	def __init__(self):
		self.side=int(input("Enter side : "))

	def area(self):
		a=self.side*self.side
		return a

sq1=squre()
area=sq1.area()
print("Area : ",area)
"""


"""class squre:
	def __init__(self):
		self.side=int(input("Enter side : "))

	def area(self):
		a=self.side*self.side
		return a

class cube(squre):
	def __init__(self):
		super().__init__()

cb=cube()
side_area=cb.area()
print("side Area ",side_area)

sq1=squre()
area=sq1.area()
print("Area : ",area) 

"""
class squre:
	def __init__(self):
		self.side=int(input("Enter side : "))

	def area(self):
		a=self.side*self.side
		return a

class cube(squre):
	def __init__(self):
		super().__init__()

	def volume(self):
		return self.side**3

	def sur_area(self):
		return 6*self.side

cb=cube()
side_area=cb.area()
print("side Area ",side_area)

sq1=squre()
area=sq1.area()
print("Area : ",area) 

