#ForLoop Key value pair

CustomerDetails = {

    "Name": "Bala",
    "age" : 36,
    "isActive": True,
    "City": "Chennai",
    "Country": "US"
    }
CustomerDetails.setdefault("Country", "India") #add key if no keys present

print(CustomerDetails)


for key in CustomerDetails:
    print(key)

for value in CustomerDetails.values():
    print(value)

for i, j in CustomerDetails.items():
    print(i + " --->"+ str(j))

if "City" in CustomerDetails:
    print("Key present")

CustomerDetails_1 = CustomerDetails.copy()

print(CustomerDetails_1)

Name = "Bala"

L1 = ["a", "b", "c"]

studnets = dict.fromkeys(L1, 100)

print(studnets)




