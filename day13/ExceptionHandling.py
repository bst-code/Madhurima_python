
# Exception -
# 1. Compile time or Checked exception
# 2. Runtime or unchecked exception -- Try catch block

#
# for i in range(100):
#     print(i)

L1 = [1, 2, 3, 4, 5]
try:
    print(L1[62])
except IndexError as e:
    print("Please enter number less than", len(L1))
except Exception as e:
    print(e)
else:
    print("No exception raised")
finally:
    print("Finally will execute always...")



