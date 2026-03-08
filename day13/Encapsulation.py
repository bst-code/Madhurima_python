
#Encapsulation is the process of wrapping data and methods together in a class and restricting direct access to the data.
#Data is hidden from outside access.
#Access to data is controlled using methods (getter and setter).
#Helps in data security and better code organization.

class Calculator:

    i = 10
    __j = 20
    __age = 90

    #getter
    def getAge(self):
        return self.__age

    #setter method
    def setAge(self, age):
        self.__age = age

    def sum(self) :
        print("Calculator -- Sum")
        total = self.i + self.__j
        print("Total is :", total)
        print("Age is ",self.__age)

    @staticmethod
    def checkObj():
        obj = Calculator()
        print(obj.i)
        print(obj.__j)

Calculator.checkObj()

obj = Calculator()
print(obj.i)
obj.sum()
print("My age is ",obj.getAge()) #90

obj.setAge(100) #sets age as 100

print("My age is ",obj.getAge()) #100
