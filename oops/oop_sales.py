class Amount():
	def __init__(self):
		self.principle=int(input("Enter Principle Amount : "))
		self.rate=int(input("Enter rate : "))
		self.time=int(input("Enter Time : "))

	def show(self):
		Total=self.principle*self.rate*self.time/100
		print(self.principle)
		print(self.rate)
		print(self.time)
		print("Total = ",Total)

def dwrite(value1):
	file=open("Amount.txt","a")
	detail_row="{}".format(value1)
	file=write(detail_row)
	file.close()

def dread():
	file=open("Amount.txt","r")
	Amount_Total=file.read()
	print(Amount_Total)


g1=Amount()
g1.show()