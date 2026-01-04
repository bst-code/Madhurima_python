#prime number
'''
number = int(input("Enter the number")) # 7

for i in range(2,number): # 2,3,4,5,6
    if number % i == 0:
        print("Given number is not a prime number")
        break
else:
    print("Given number is a prime number")
'''

#Print Primenumber between 1 to 100

PrimeNos = []

for i in range(2,100):
 number = i
 for j in range(2,number): # 2,3,4,5,6
    if number % j == 0:
            break
 else:
     PrimeNos.append(number)
    #print("Prime number",number)


print(PrimeNos)


