#from file1 import *
import file1 as f

x = int(input("Enter your interger : "))
y = f.fact(x)
print("factorial of {} = {}".format(x,y))