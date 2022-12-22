"""device='sunny's iphone'

name="Chetan"
print("name=",name)
print(type(name))
"""

            #STRING
"""

name="Chetan Malviya"
age="22"
contact="7898853184"
Email="malviyachetan26805@gmail.com"

print("Hi my name is "+name+" I am "+age+" year old. my contact details are phone: "+contact+" and email: "+Email)
"""


"""
print("hi my name is {}. I am {} year old. my contact details are phone {} and email {}.".format(name,age,contact,Email))
"""



"""
para=' Qty1="Twinkle, twinkle, little star," \nQty=2"How I wonder what you are." \nQty=3"Up above the world so high," \nQty="4Like a diamond in the sky." '
print(para)

"""




            #unique id defind
"""

user_string=input("Enter your string")
x=" "  
for i in user_string:
	if i ==" . ":
		print(x)
		print("\n")
		x=" "
	else:
		x=x+i

x=ord("A")
print(x)

"""

"""

user_string=input("Enter your string")
x=""
for i in user_string:

	j=ord(i)
	k=ord(".")
	print("j=",j)
	print("k",k)
	print("-------------------------")
	if k==j:
		print(x)
		print("\n")
		x=""
	else:
		x=x+i 

"""

   
      #concatinate


"""
user_string=input("Enter your string ")
x=" "
for i in user_string:
	if i==".":
		print(x)
		x=" "
	else:
		x=x+i
print(x)

"""
            #UPPER CASH 
"""
str1="my name is vegeta"
print(str1)
str2=str1.upper()
print(str1,str2)
str3=str1.lower()
print(str1,str2,str3)
	"""
         
         #count
"""

str2=input("Enter your ")
count=0
for i in str2:
	count=count+1

print(count)   """


"""           #cAmel cash

value1=input("Enter the string:")
value2=" "
for i in range(len(value1)):
	if i !=1:
		value2=value2+value1[i].lower()
else:
	value2=value2+value1[i].upper()
print("user given value=",value1)
print("camelcase of given=",value2)

"""

"""
                #factorial
x=int(input("Enter no:"))
y=1
for i in range(1,x+1):
	y=y*i
print("Factional of {} is {}" . format (x,y))

"""