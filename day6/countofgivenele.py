ele = 4
count = 0
L1 = [1,2,3,4,3,4,3,5,6]
for i in L1:
    if(i==ele):
       count = count + 1
else:
    if count == 0:
        print("Element not found in the list")
    else:
        print("count of given element", count)
