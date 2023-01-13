Average=open("Average.txt","a")
English=int(input("Enter english marks: "))
Hindi=int(input("Enter Hindi marks: "))
Maths=int(input("Enter maths marks: "))
Average_Marks="Sub marks are\n English: {}\n Hindi: {}\n maths: {}\n".format(English,Hindi,Maths)

print(Average_Marks)
Average.write(Average_Marks)
Avg=str(English+Hindi+Maths/3)

print(Avg)
Avg.write(Avg)
Average.close()

Average=open("Average.txt","r")
data=Average.read()
print(data)
Average.close()



