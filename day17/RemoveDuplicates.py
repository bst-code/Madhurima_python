# ==========================================
# PROGRAM: Remove Duplicates from List
# ==========================================

# METHOD 1: Using SET (Most Common & Efficient)
# ==============================================
print("=" * 50)
print("METHOD 1: Using SET")
print("=" * 50)

original_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
print(f"Original List: {original_list}")

# Convert list to set to remove duplicates
unique_items = set(original_list)
print(f"Using set(): {unique_items}")

# Convert back to list if needed
unique_list = list(set(original_list))
print(f"Convert back to list: {unique_list}")
print()

# ------- EXPLANATION -------
# - Set removes duplicates automatically (no duplicate allowed in sets)
# - Fast and efficient for large lists
# - NOTE: Order is NOT preserved
# - Time Complexity: O(n)
# - Space Complexity: O(n)
print("✓ ADVANTAGE: Very fast and simple")
print("✗ DISADVANTAGE: Order of elements is lost")
print()


# METHOD 2: Using FOR LOOP (Preserves Order)
# ============================================
print("=" * 50)
print("METHOD 2: Using FOR LOOP (Order Preserved)")
print("=" * 50)

original_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
print(f"Original List: {original_list}")

unique_list = []
for item in original_list:
    if item not in unique_list:  # Check if item already exists
        unique_list.append(item)

print(f"Result: {unique_list}")
print()

# ------- EXPLANATION -------
# - Iterate through each element in original list
# - Check if element already exists in unique_list
# - Only add if it's NOT already present
# - Order is PRESERVED
# - Time Complexity: O(n²) - because "in" operation checks each element
# - Space Complexity: O(n)
print("✓ ADVANTAGE: Order is preserved")
print("✗ DISADVANTAGE: Slower for large lists (O(n²))")
print()


# METHOD 3: Using DICTIONARY (Preserves Order in Python 3.7+)
# ===========================================================
print("=" * 50)
print("METHOD 3: Using DICTIONARY")
print("=" * 50)

original_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
print(f"Original List: {original_list}")

# Method 3a: Using dict.fromkeys()
unique_list = list(dict.fromkeys(original_list))
print(f"Using dict.fromkeys(): {unique_list}")
print()

# ------- EXPLANATION -------
# - dict.fromkeys() creates a dictionary with list elements as keys
# - Dictionary keys are unique automatically
# - In Python 3.7+, dictionaries maintain insertion order
# - convert back to list using list()
# - Time Complexity: O(n)
# - Space Complexity: O(n)
print("✓ ADVANTAGE: Order preserved, Fast")
print("✓ Most Pythonic approach")
print()


# METHOD 4: Using LIST COMPREHENSION with INDEX (Preserves Order)
# ===============================================================
print("=" * 50)
print("METHOD 4: Using LIST COMPREHENSION with INDEX")
print("=" * 50)

original_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
print(f"Original List: {original_list}")

# Keep only first occurrence of each element
unique_list = [item for index, item in enumerate(original_list) if original_list.index(item) == index]
print(f"Result: {unique_list}")
print()

# ------- EXPLANATION -------
# - enumerate() gives us (index, item) for each element
# - original_list.index(item) returns the FIRST occurrence index
# - If current index == first occurrence index, keep it
# - Otherwise, it's a duplicate, so skip it
# - Order is PRESERVED
# - Time Complexity: O(n²) - index() searches through list
# - Space Complexity: O(n)
print("✓ ADVANTAGE: Pythonic, Order preserved")
print("✗ DISADVANTAGE: Slower for large lists")
print()


# METHOD 5: FUNCTION with OPTION to PRESERVE ORDER
# =================================================
print("=" * 50)
print("METHOD 5: CUSTOM FUNCTION (BEST PRACTICE)")
print("=" * 50)

def remove_duplicates(lst, preserve_order=True):
    """
    Remove duplicates from a list
    
    Parameters:
    -----------
    lst : list
        Input list with potential duplicates
    preserve_order : bool
        If True: Preserves original order (slower)
        If False: Uses set (faster, but order is lost)
    
    Returns:
    --------
    list
        List without duplicates
    """
    if preserve_order:
        # Method: Dictionary (best balance)
        return list(dict.fromkeys(lst))
    else:
        # Method: Set (fastest)
        return list(set(lst))


# Test with different lists
list1 = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
list2 = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
list3 = [10, 20, 10, 30, 20, 40]

print("Test 1 - Numbers (Preserve Order):")
print(f"Original: {list1}")
print(f"Result:   {remove_duplicates(list1, preserve_order=True)}")
print()

print("Test 2 - Strings (Preserve Order):")
print(f"Original: {list2}")
print(f"Result:   {remove_duplicates(list2, preserve_order=True)}")
print()

print("Test 3 - Numbers (Fast, Don't Preserve Order):")
print(f"Original: {list3}")
print(f"Result:   {remove_duplicates(list3, preserve_order=False)}")
print()


# COMPARISON OF ALL METHODS
# =========================
print("=" * 50)
print("COMPARISON TABLE")
print("=" * 50)

comparison = """
╔══════════════════╦════════════╦═════════════╦═══════════════════╗
║ Method           ║ Time Comp  ║ Preserves   ║ Best For          ║
║                  ║            ║ Order       ║                   ║
╠══════════════════╬════════════╬═════════════╬═══════════════════╣
║ 1. set()         ║ O(n)       ║ NO          ║ Speed Priority    ║
║ 2. For Loop      ║ O(n²)      ║ YES         ║ Small Lists       ║
║ 3. dict.fromkeys ║ O(n)       ║ YES (3.7+)  ║ RECOMMENDED       ║
║ 4. Comprehension ║ O(n²)      ║ YES         ║ Learning/Simple   ║
║ 5. Custom Func   ║ O(n)       ║ Optional    ║ Flexible/Reusable ║
╚══════════════════╩════════════╩═════════════╩═══════════════════╝
"""
print(comparison)
print()


# PRACTICAL EXAMPLES
# ==================
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Removing duplicate student IDs
print("\n📚 Example 1: Student ID Database")
student_ids = [101, 102, 101, 103, 102, 104, 105]
print(f"Original Student IDs: {student_ids}")
print(f"Unique Student IDs:   {remove_duplicates(student_ids)}")

# Example 2: Removing duplicate emails
print("\n📧 Example 2: Email List")
emails = ['user1@gmail.com', 'user2@gmail.com', 'user1@gmail.com', 'user3@gmail.com']
print(f"Original Emails: {emails}")
print(f"Unique Emails:   {remove_duplicates(emails)}")

# Example 3: Removing duplicate words from sentence
print("\n📝 Example 3: Words in Sentence")
sentence = "Python is great Python is awesome Python"
words = sentence.split()  # ['Python', 'is', 'great', 'Python', 'is', 'awesome', 'Python']
print(f"Original Words: {words}")
print(f"Unique Words:   {remove_duplicates(words)}")

# Example 4: Removing duplicate scores
print("\n🎮 Example 4: Game Scores")
scores = [100, 150, 100, 200, 150, 250, 100]
print(f"Original Scores: {scores}")
print(f"Unique Scores:   {remove_duplicates(scores)}")
print()


# REAL-WORLD SCENARIO
# ===================
print("=" * 50)
print("REAL-WORLD SCENARIO: Data Cleaning")
print("=" * 50)

# Simulating a list of user inputs with duplicates
user_entries = [
    'apple',
    'banana',
    'apple',      # duplicate
    'cherry',
    'banana',     # duplicate
    'date',
    'apple'       # duplicate
]

print(f"Raw User Entries: {user_entries}")
print(f"Count: {len(user_entries)} items")

cleaned_entries = remove_duplicates(user_entries)
print(f"\nCleaned Entries: {cleaned_entries}")
print(f"Count: {len(cleaned_entries)} unique items")
print(f"Duplicates removed: {len(user_entries) - len(cleaned_entries)}")
print()

# Count occurrences of duplicates
print("Duplicate Analysis:")
for item in cleaned_entries:
    count = user_entries.count(item)
    if count > 1:
        print(f"  '{item}' appeared {count} times (removed {count-1} duplicates)")

