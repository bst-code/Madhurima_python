#Swapping

a = 10
b = 30
'''
temp = a #thrid variable
a=b
b= temp
'''

#Without using third variable
a = a+b # 40
b = a-b #10
a = a-b #30


print("a--> ",a)
print("b--> ",b)

#Python logic to swap data 
i = 100
j = 300

i,j = j,i

print("i ",i)
print("j ",j)

