#Dict - Key = Value pair
# A dictionary in Python is a collection of key–value pairs.

CustomerDetails = {

    "Name": "Bala",
    "age" : 36,
    "isActive": True,
    "City": "Chennai"
    }


print(CustomerDetails.keys()) # give all keys
print(CustomerDetails.values()) # gives all values
print(CustomerDetails.items()) # gives both key value pair


print(CustomerDetails)

print(CustomerDetails["age"])
print(CustomerDetails.get("age1"))


CustomerDetails["MobileNo"] = '96006667474794' #Add new key
CustomerDetails["age"] = 46 # update value in existing key

print(CustomerDetails)

data = CustomerDetails.pop("Name")
print('data ---->', data)

print(CustomerDetails)
CustomerDetails.popitem()
print(CustomerDetails)

del CustomerDetails["age"]
print(CustomerDetails)

CustomerDetails.clear()
print(CustomerDetails)






