#tuple for loop

T1 = (1,2,3,5,7,9,10,12,16,20)# Fixed Data
L1 = [] # Dynamic Data
for i in T1:
    print("Welcome", i)
    if i%2 == 0:
        L1.append(i)

print(L1)
print(len(L1))

        
