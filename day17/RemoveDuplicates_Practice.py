# ==========================================
# SIMPLE PRACTICE PROGRAMS
# Remove Duplicates - Multiple Examples
# ==========================================

print("🎓 PRACTICE PROGRAM 1: Simple Set Method")
print("=" * 50)

# Quick and simple approach
numbers = [5, 2, 8, 2, 9, 1, 5, 5]
print(f"Original: {numbers}")

result = list(set(numbers))
print(f"Result:   {result}")
print()


print("🎓 PRACTICE PROGRAM 2: For Loop Method")
print("=" * 50)

fruits = ['apple', 'banana', 'apple', 'cherry', 'banana']
print(f"Original: {fruits}")

unique_fruits = []
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

print(f"Result:   {unique_fruits}")
print()


print("🎓 PRACTICE PROGRAM 3: Dict Method (RECOMMENDED)")
print("=" * 50)

colors = ['red', 'blue', 'red', 'green', 'blue', 'yellow']
print(f"Original: {colors}")

result = list(dict.fromkeys(colors))
print(f"Result:   {result}")
print()


print("🎓 PRACTICE PROGRAM 4: Interactive Input")
print("=" * 50)

# Get list from user
user_input = input("Enter numbers separated by comma (e.g., 1,2,2,3): ")
numbers = [int(x.strip()) for x in user_input.split(',')]

print(f"Original List: {numbers}")
unique_list = list(dict.fromkeys(numbers))
print(f"Unique List:   {unique_list}")
print(f"Removed:       {len(numbers) - len(unique_list)} duplicates")
print()


print("🎓 PRACTICE PROGRAM 5: Function with Count")
print("=" * 50)

def remove_and_count_duplicates(lst):
    """Remove duplicates and show statistics"""
    original_length = len(lst)
    unique_list = list(dict.fromkeys(lst))
    unique_length = len(unique_list)
    duplicates_count = original_length - unique_length
    
    print(f"Original items:  {original_length}")
    print(f"Unique items:    {unique_length}")
    print(f"Duplicates:      {duplicates_count}")
    print(f"Result:          {unique_list}")
    
    return unique_list

print("\nExample 1:")
remove_and_count_duplicates([1, 2, 2, 3, 3, 3])

print("\nExample 2:")
remove_and_count_duplicates(['a', 'b', 'a', 'c', 'b'])
print()


print("🎓 PRACTICE PROGRAM 6: Find Duplicated Elements Only")
print("=" * 50)

my_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Original List: {my_list}")

# Method: Find which elements appear more than once
duplicated_items = []
for item in set(my_list):
    if my_list.count(item) > 1:
        duplicated_items.append(item)

print(f"Duplicated Elements: {duplicated_items}")
print()


print("🎓 PRACTICE PROGRAM 7: Remove Duplicates & Sort")
print("=" * 50)

numbers = [5, 2, 8, 2, 9, 1, 5, 5]
print(f"Original:        {numbers}")

unique_sorted = sorted(list(dict.fromkeys(numbers)))
print(f"Unique & Sorted: {unique_sorted}")
print()


print("🎓 PRACTICE PROGRAM 8: Compare Methods")
print("=" * 50)

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Original: {my_list}\n")

# Method 1: Set
result1 = list(set(my_list))
print(f"Method 1 (set):           {result1}")

# Method 2: For loop
result2 = []
for item in my_list:
    if item not in result2:
        result2.append(item)
print(f"Method 2 (for loop):      {result2}")

# Method 3: Dict
result3 = list(dict.fromkeys(my_list))
print(f"Method 3 (dict.fromkeys): {result3}")

print("\n✓ Methods 2 & 3 preserve order")
print("✗ Method 1 doesn't preserve order")
print()


print("🎓 PRACTICE PROGRAM 9: Real Data Example")
print("=" * 50)

# Student scores list (with duplicates)
student_scores = [85, 90, 85, 92, 88, 90, 95, 85, 92]
print(f"All Scores:        {student_scores}")

unique_scores = list(dict.fromkeys(student_scores))
print(f"Unique Scores:     {unique_scores}")
print(f"Number of Unique Scores: {len(unique_scores)}")

# Find which scores appear multiple times
print("\nScore Frequency:")
for score in unique_scores:
    count = student_scores.count(score)
    if count > 1:
        print(f"  Score {score}: appears {count} times")
print()


print("🎓 PRACTICE PROGRAM 10: Remove Duplicates from Strings")
print("=" * 50)

# Remove duplicate characters from word
word = "mississippi"
print(f"Original word: {word}")

unique_chars = list(dict.fromkeys(word))
print(f"Unique chars: {unique_chars}")
print(f"Unique word:  {''.join(unique_chars)}")

