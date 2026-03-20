
#read data from txt file

# open("File name", "mode")
'''
file = open("Sample.txt",'r')
data = file.read()
# data = file.readline()
# data = file.readlines()
print(data)
file.close()
'''

#Write - create file and write
f = open("../Data/Bspark_0.txt",'w')
f.write("This is line 1 \n")
f.write("This is line 2 \n")
f.write("This is line 3")
f.close()

#append or update existing file
f = open("../Data/Bspark_0.txt",'a')
f.write("\nThis is line 4 \n")
f.write("This is line 5 \n")
f.close()

f = open("../Data/Bspark_0.txt",'r')
data = f.read()
print(data)
f.close()

# With statement examples - dont need to close the file manually

with open("./Data1/Bspark_2.txt",'w') as f:
    f.write("This is line 10 \n")
    f.write("This is line 11")

with open("./Data1/Bspark_2.txt",'a') as f:
    f.write("\nThis is line 12 \n")
    f.write("This is line 13 \n")

with open("./Data1/Bspark_2.txt",'r') as f1:
    data = f1.read()
    print(data)
    
# Get the count of each word for each line (multiple line)