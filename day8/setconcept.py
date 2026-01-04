#Set
#No duplicate
#Unordered
#Mutable --> Update data

names = {1,0,2,9,10,3,4,5,6,6,6,6}

print(type(names))

email = set([1,2,3,3,3,0])
print(type(email))
print(email)
email.add(8)
print(email)
email.update([9,9,9])
print(email)

email.remove(3)
email.discard(111)
print(email)

email.clear()

print(email)



