import time as t 
start_time = t.time()
i = int(input("Enter fact :"))
# start_time = t.time()
fact = 1
if i == 0 or i ==1:
	print("{} is factorial of {}".format(fact,i))
else:
	for j in range(1,i+1):
		fact = fact*j
	print("{} is factorial of {}". format(fact,i))
end_time = t.time()
total_time=end_time-start_time
print(total_time)
