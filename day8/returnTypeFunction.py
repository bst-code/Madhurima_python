#Return Type

def getAge(DOB_year):
    currentYear = 2026
    output = currentYear - DOB_year
    print(output)
    return output

def checkVoting(age):
    if age >=18:
        print("Eligible for voting ")
    else:
        print("Not Eligible for voting")
        

Myage = getAge(2009)
checkVoting(Myage)
# (OR)
checkVoting(getAge(1989))

