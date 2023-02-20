"""class circle:
	def __init__(self,radius):
		self.radius=radius
	def area(self):
		return 3.14*self.radius*self.radius
	def circumsference(self):
		return 3.14*2*self.radius

def dwrite(x):
	file=open("detail.txt","a")
	file.write(x)
	file.close()
	print("write operation")

def dread():
	pass

for i in range(1,101):
	var1=circle(i)
	var2=var1.area()
	var3=var1.circumsference()
	var4="{},{},{}\n".format(var1.radius,var2,var3)
	dwrite(var4)
	print("Radius of circle = {} cm".format(var1.radius))
	print("Area of circle = {} sq cm".format(var2))
	print("circumsference of circle = {} cm".format(var3))
	print("---------------------------------------")
"""
class circle:
	def __init__(self,radius):
		self.radius=radius
	def area(self):
		return 3.14*self.radius*self.radius
	def circumsference(self):
		return 3.14*2*self.radius

def dwrite(x):
	file=open("detail.txt","a")
	file.write(x)
	file.close()
	print("write operation")
	x=data.splite("\n")
	print(x)

# def dread():
# 	pass

"""for i in range(1,101):
	var1=circle(i)
	var2=var1.area()
	var3=var1.circumsference()
	var4="{},{},{}\n".format(var1.radius,var2,var3)
	dwrite(var4)
	print("Radius of circle = {} cm".format(var1.radius))
	print("Area of circle = {} sq cm".format(var2))
	print("circumsference of circle = {} cm".format(var3))
	print("---------------------------------------")
"""
def dread():
	file=open("detail.txt","r")
	data=file.read()
	print(data)

dread()


