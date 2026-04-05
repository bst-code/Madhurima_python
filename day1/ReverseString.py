# Different Methods to Reverse a String

# Method 1: Using String Slicing (Most Pythonic & Efficient)
# Syntax: string[start:stop:step]
# step = -1 means go backwards
string = "Hello"
reversed_string = string[::-1]
print("Method 1 (Slicing):")
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")
print()

# Method 2: Using a Loop
# Iterate from the end to the beginning
string = "Python"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string  # Add each character to the beginning
print("Method 2 (Loop):")
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")
print()

# Method 3: Using reversed() Function
# reversed() returns an iterator
string = "World"
reversed_string = "".join(reversed(string))
print("Method 3 (reversed() function):")
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")
print()

# Method 4: Using Recursion
# A function that calls itself to reverse a string
def reverse_recursive(string):
    if len(string) == 0:  # Base case: empty string
        return string
    else:
        return reverse_recursive(string[1:]) + string[0]  # Call function + first character

string = "Coding"
reversed_string = reverse_recursive(string)
print("Method 4 (Recursion):")
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")
print()

# Method 5: Using a Loop (Backward Iteration)
# Iterate the string backwards using range()
string = "Python"
reversed_string = ""
for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
print("Method 5 (Loop with Backward Range):")
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")
print()

# Practical Example: Check if a string is a Palindrome
# A palindrome reads the same forwards and backwards
def is_palindrome(string):
    # Remove spaces and convert to lowercase for comparison
    clean_string = string.replace(" ", "").lower()
    return clean_string == clean_string[::-1]

test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
print("Palindrome Check:")
for test in test_strings:
    result = is_palindrome(test)
    print(f"'{test}' is palindrome: {result}")

