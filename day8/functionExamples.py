a = 10
b = 20
print(a+b)

a = 100
b = 200
print(a+b)
print(type(a))

# A function is a block of reusable code that performs a specific task.
#It is independent and not tied to any object.
# Inbuild functions - len, type, sum etc

def add():
    a = 100
    b = 200
    print(a+b)
    
add()
add()

def add1(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

add1(10,40)
add1(50,50)
add1(40,40)
sub(900,100)

def getAge(DOB_year):
    currentYear = 2026
    output = currentYear - DOB_year
    print(output)

getAge(2009)
getAge(1989)
for i in range(5):
    year = int(input("Enter Birth year "))
    getAge(year)




























