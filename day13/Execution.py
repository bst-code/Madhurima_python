from day13.Encapsulation import Calculator

class test:

    @staticmethod
    def checkObj():
        obj = Calculator()
        print(obj.i)
        print(obj.__j)

test.checkObj()