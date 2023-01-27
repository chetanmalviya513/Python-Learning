"""
import sample1
#calculating permutation
n,r=int(input("Enter value N : ")),int(input("Enter value of R : "))

if n > r or n==r :
	result=sample1.fact(n)/sample1.fact(n-r)
	print(result)
else:
	print("invalid result")
"""
"""
#import sample1
#calculating permutation
import sample1 as s
n,r=int(input("Enter value N : ")),int(input("Enter value of R : "))

if n > r or n==r :
	result=s.fact(n)/s.fact(n-r)
	print(result)
else:
	print("invalid result")
"""
from sample1 import *
n,r=int(input("Enter value N : ")),int(input("Enter value of R : "))

if n > r or n==r :
	result=fact(n)/fact(n-r)
	print(result)
else:
	print("invalid result")
