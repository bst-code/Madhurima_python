#Set functions

s1 ={10,40,60,80}

print(60 in s1)
print(600 in s1)
print(600 not in s1)
print(60 not in s1)

s1.clear()
print(s1)

#Set operations

s1 ={1,2,3,4,5,6}
s2 ={1,2,7,8,9}

print( s1 | s2) #Union --get all data from both the sets
print( s1 & s2) #Intersection - Get only common data

print(s1 - s2) # Difference {3, 4, 5, 6}

print(s1 ^ s2) #Symmetric Difference
