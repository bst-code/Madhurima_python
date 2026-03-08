L1 = [1,2,3,4,5,6]  # Bala
D1 = {}
for item in L1:
    if item not in D1:
        D1[item] = item ** 2


t1 = (1,2,3)
t2 = t1
print(t2)

t1 +=(4,)
print(t1)
print(t1==t2)

name = "Bala"
if name == "Bala":
    print("Passed")
else:
    print("Failed")

print((name == "Bala"))

#----------------

customers = {"FirstName": "Shivya", "Age": 18}
print(customers)
print(customers.get("FirstName"))
del customers["FirstName"]
print("loc---->",customers["LOC"])

S1 = "WaterSkiing is thrilling! "
print(S1.split("i"))


