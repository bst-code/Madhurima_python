#List Examples

L1 = [100,900,300,400,500]
print(L1)
print('Inbuild SUM function output', sum(L1))

total = 0

for i in range(1,4):
    #print(i, L1[i])
    total = total + L1[i]
    print(i, ":", total)

    total = total + L1[i]*10
    print("total * 10-->",total)
    
    
print("our logic to get sum of all records in the List",total)
