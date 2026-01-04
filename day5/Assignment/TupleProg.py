#Even no in tuple

T1 = (1,2,3,4,5,6)
T2 =()

for i in T1:
    if(i%2==0):
        T2 = T2+(i,)
print(T2)
