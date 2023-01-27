#set notes
"""
star={2,4,6,2,11,12}
print(star)
"""

star={2,4,6,2,11,12,"yes","no","no",2.4,255,0+1j}
print(star)
star.add("23")
print(star)
star.pop()
print(star)
star.remove("23")
print(star)
star.discard("no")
print(star)
del(star)