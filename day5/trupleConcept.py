#Truple - Immutable

#L1 = [1,2,3,4]
#L1[0] = 100
#print(L1)

#A tuple in Python is a collection data type used to store multiple values in a single variable.
#Ordered, Immutable (Not changable), Allow Duplicate, Allow different Data types, Faster than List,
#Fixed Data


T1 =(1,2,3,4,5,5,6,6,6,"Bala", True)

print(T1)
print(type(T1))

print(T1[1])
print(T1[2:5])

#Methods - count and index

print(T1.count(6))
print(T1.index(6))

T2 =(90,40,80,1,2,3,4,5,5,6,6,6,0)

print(sum(T2))
print(min(T2))
print(max(T2))
print(len(T2))

L2 = sorted(T2)
print(type(L2))

T3 = tuple(L2)
print(T3)

print(all(T3))
print(any(T3))





























