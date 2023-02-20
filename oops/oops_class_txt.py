class circle:
	def __init__(self):
		self.radius=int(input("Enter The radious : "))
	def area(self):
		return 3.14*self.radius*self.radius
	def circumsference(self):
		return 3.14*2*self.radius

def dwrite(var1,var2,var3):
	file=open("detail.txt","a")
	datarow="{},{},{},\n".format(var1,var2,var3)
	file.write(datarow)
	file.close()
	print("Write operation done sucessfully")

c1=circle()
area=c1.area()
circumsference=c1.circumsference()
radius1=c1.radius
var1="Radius : {} cm".format(radius1)
var2="Area : {} sq cm".format(area)
var3="Circumsference : {} cm".format(circumsference)
dwrite(var1,var2,var3)


