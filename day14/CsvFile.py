import csv

with open('data1.csv','r') as f:
    reader = csv.DictReader(f)

    print("Headers name ",reader.fieldnames)
    #print(reader.line_num)

    for row in reader:
        print("My Name is ",row['Name'])
        print("My age is ",row['Age'])
        print("My City is ",row['City'])
        print('--------------------------')

# Open and write to the CSV file
with open('data2.csv', mode='a' ,newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Bala',  '30', 'Chennai'])
     writer.writerow(['John',  '25', 'Mumbai'])