
from abc import ABC, abstractmethod

#RBI --- #HDFC # ICICI
#RBI --> Interface ---> Abstract class #ABC -- Abstract Base Class (ABC)

#We cant create obj for abstract class directly and use
#We need to create obj for subclass or child to use the abstract method of abstract class

class RBI(ABC):  #Abstract class ---Abstract method

    country = "India"
    @abstractmethod
    def getCustomerInfo(self):
       pass
    @abstractmethod
    def getCurrencyType(self):
        pass
    def getCountryCode(self):   #Non abstract method
        print("RBI get country code as 91")
    @abstractmethod
    def getEmail(self):
        pass
#---------------------------------------------------------------------------------
class HDFC(RBI):
    def getEmail(self):
        print("HDFC get email as bala@test.com")

    def getCustomerInfo(self):
        print(self.country, " HDFC get customer info like aadhar card")

    def getCurrencyType(self):
        print("HDFC get currency type as rupee")

    def getMobileNumber(self):
        print("HDFC get mobile number")
#---------------------------------------------------------------------------------

class ICICI(RBI):
    def getCustomerInfo(self):
        print("ICICI get customer info like aadhar card")

    def getCurrencyType(self):
        print("ICICI get currency type as rupee")


obj = HDFC()
obj.getCustomerInfo()
obj.getCurrencyType()
obj.getMobileNumber()
print(obj.country)
obj.getCountryCode()
obj.getEmail()
