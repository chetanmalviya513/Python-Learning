def bill_entry():
	Cus_Name=input("Enter Custmer Name : ")
	product=input("Enter Product Name : ")
	Price=int(input("Enter Product Price : "))
	Quantity=int(input("Enter Product Quantity : "))
	Total=product*Price
	file.open("Bill.txt","a")
	Entry="{},{},{},{}\n".format(product,Price,Quantity,Total)
	file.write(Entry)
	file.close()
	print("Custmer Bill Recorded Sucessfull ")

def Re_entry():
	choice=input("Enter Y for Adding Another Custmer Bll or N for Exit : ")
	if choice=="Y" or choice=="y":
		return True
	elif choice=="N" or choice=="n":
		return False
	else:
Re_entry()
		

		
		
