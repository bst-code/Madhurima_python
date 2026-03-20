
import random, math

print(random.random())
print(random.randint(10000, 99999))

my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")
random.shuffle(my_list) # Shuffles the list in-place
print(f"Shuffled list: {my_list}")

my_list = ["apple", "banana", "cherry", "date"]
random_item = random.choice(my_list)
print(random_item)

print(math.pi)
print(math.sqrt(9))
print(math.factorial(5))

# Ceil: Round up
print(math.ceil(4.2))    # Output: 5

# Floor: Round down
print(math.floor(4.8))   # Output: 4
# Factorial: 3! = 3*2*1
print(math.factorial(3)) # Output: 6
# ISQRT: Integer square root of 27
print(math.isqrt(27))    # Output: 5 (sqrt is 5.19..., floor is 5)
