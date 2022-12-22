"""student1=["Tiku","MCA1st","tiku007@gmail.com"]
print(student1[0])
print(student1)"""




student=["Tiku","MCA1st","tiku007@gmail.com"] # created a list named "student"
print(student[0])
print(student)

#add element at last
student.append("923214348348")
print(student)

#add element at specific index 
student.insert(1,"A")
print(student)

#removing the elements from last
student.pop()
print(student)

#removing specific element 
student.remove("MCA1st")
print(student)

del(student)
print(student)

