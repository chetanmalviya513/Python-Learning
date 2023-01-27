"""
student=["Chetan Malviya","Mba 1st","chetanmalviya",]
print(student[1])
print(student)

#add element at last
student.append("Khargone")
print(student)

#add element at specific index
student.insert(2,"A sec")
print(student)

#removing appenf for last
student.pop()
print(student)

#remove specific element
student.remove("A sec")
print(student)

#all delete
"""


student=[input("Enter name"),input("Enter course"),input("Enter email")]
student1=[input("Enter name"),input("Enter course"),input("Enter email")]

print("I am {}.I Am student of {}. my email id is {}".format(student[0],student[1],student[2]))
print("I am {}.I Am student of {}. my email id is {}".format(student1[0],student1[1],student1[2]))

student.insert(2,"khargone")
print(student)
student1.append("khandwa")
print(student1)