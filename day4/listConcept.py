#LIST []
#1. Ordered
#2. indexing
#3. Duplicate Allowed
#4. Mutable

students = [1,3,4,6,5,8,8,8,'a','a',True]

data = students.pop(1)
print(data) 
print(students)
print(len(students))

students.append('bala')
print(students)

students.insert(0,'Bspark')
print(students)


students.extend(['test','dev'])
print(students)

students.remove(8)
print(students)

data = students.pop(0)
print(students.pop(0))
print(students)

print(students.index('test'))
print(students.count('a'))
students.clear()

students = [1,3,4,6,5,8,8,8,2]

students.reverse()
print(students)

students.sort(reverse=True)
print(students)

students.sort()
print(students)

students1 = students.copy()
print('copied ',students1)

print(max(students1))
print(min(students1))
print(sum(students1))

print(ord('a'))
print(ord('A'))
print(ord('b'))

if ord('a')==ord('b'):
    print('equal')
else:
    print('not equal')

names = ['a','c','d','b']
names.sort()
print(names)

ages = [ord('b'),1,4,6]
print(ages)

ages.sort()
print(ages)



   









