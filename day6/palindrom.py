num = 123 # 454

original = num

rev = 0 #4

while num > 0:
    digit = num % 10
    print("digit-->", digit)
    
    rev = rev * 10 + digit
    print("rev-->", rev)
    num = num // 10

    print("num-->", num)

if(original == rev):
    print("Given number is palindrom")
else:
    print("Given number is not palindrom")
    
    
    



