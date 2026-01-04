#nested ifelse

age = 18
citizenship = True

if age >=18:
    print("Eligbile for voting")
    if(citizenship):
        print("He is citizen, so can vote") 
    else:
        print("He is not citizen of india")
else:
   print("Not Eligbile for voting") 
