"""
var1=open("intro.txt","a")
var1.write("Chetan Malviya")
var1.write("BBA SVIM-INDORE")
var1.close()

var1=open("intro.txt","r")
data=var1.read()
print(data)
var1.close()
"""
f=open("telephone.txt","a")
name=input("Enter your name : ")
age=input("Enter your age : ")
city=input("Enter your city : ")
details="Hi I am {}.\nI am {} year old.\nI live in {}.".format(name,age,city)
print(details)
f.write(details)
f.close()

f=open("telephone.txt","r")
data=f.read()
print(data)
f.close()