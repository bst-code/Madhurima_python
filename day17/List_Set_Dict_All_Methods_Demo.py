# =============================================
# LIST, SET, AND DICTIONARY - COMPLETE DEMO
# =============================================

print("╔" + "="*60 + "╗")
print("║" + " "*15 + "LIST, SET, AND MAP DEMONSTRATION" + " "*12 + "║")
print("╚" + "="*60 + "╝")
print()

# ============================================================
# PART 1: LIST METHODS DEMONSTRATION
# ============================================================

print("=" * 70)
print("PART 1: LIST - 23 METHODS")
print("=" * 70)
print()

# Create a list
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}\n")

# 1. append()
print("1️⃣ append() - Add single element")
my_list.append(6)
print(f"   After append(6): {my_list}\n")

# 2. extend()
print("2️⃣ extend() - Add multiple elements")
my_list.extend([7, 8, 9])
print(f"   After extend([7,8,9]): {my_list}\n")

# 3. insert()
print("3️⃣ insert() - Insert at specific position")
my_list.insert(2, 99)
print(f"   After insert(2, 99): {my_list}\n")

# 4. remove()
print("4️⃣ remove() - Remove by value (first occurrence)")
my_list.remove(99)
print(f"   After remove(99): {my_list}\n")

# 5. pop()
print("5️⃣ pop() - Remove and return by index")
removed = my_list.pop()  # Remove last
print(f"   pop() returned: {removed}")
print(f"   After pop(): {my_list}\n")

# 6. clear()
print("6️⃣ clear() - Remove all elements")
test_list = [10, 20, 30]
print(f"   Before clear(): {test_list}")
test_list.clear()
print(f"   After clear(): {test_list}\n")

# 7. index()
print("7️⃣ index() - Find position of element")
numbers = [10, 20, 30, 20, 40]
idx = numbers.index(20)
print(f"   numbers = {numbers}")
print(f"   index(20) = {idx} (first occurrence)\n")

# 8. count()
print("8️⃣ count() - Count occurrences")
count = numbers.count(20)
print(f"   numbers.count(20) = {count}\n")

# 9. sort()
print("9️⃣ sort() - Sort in-place")
unsorted = [5, 2, 8, 1, 9]
print(f"   Before: {unsorted}")
unsorted.sort()
print(f"   After sort(): {unsorted}")
unsorted.sort(reverse=True)
print(f"   After sort(reverse=True): {unsorted}\n")

# 10. reverse()
print("🔟 reverse() - Reverse in-place")
rev_list = [1, 2, 3, 4, 5]
print(f"   Before: {rev_list}")
rev_list.reverse()
print(f"   After reverse(): {rev_list}\n")

# 11. copy()
print("1️⃣1️⃣ copy() - Create shallow copy")
original = [1, 2, 3]
copied = original.copy()
copied[0] = 999
print(f"   Original: {original}")
print(f"   Copied: {copied}\n")

# 12. len()
print("1️⃣2️⃣ len() - Get length")
my_list = [10, 20, 30, 40, 50]
print(f"   {my_list}")
print(f"   len(list) = {len(my_list)}\n")

# 13. min()
print("1️⃣3️⃣ min() - Find minimum")
numbers = [5, 2, 8, 1, 9]
print(f"   {numbers}")
print(f"   min(list) = {min(numbers)}\n")

# 14. max()
print("1️⃣4️⃣ max() - Find maximum")
print(f"   {numbers}")
print(f"   max(list) = {max(numbers)}\n")

# 15. sum()
print("1️⃣5️⃣ sum() - Sum all elements")
print(f"   {numbers}")
print(f"   sum(list) = {sum(numbers)}\n")

# 16. any()
print("1️⃣6️⃣ any() - Check if any element is True")
values = [False, False, True, False]
print(f"   {values}")
print(f"   any(list) = {any(values)}\n")

# 17. all()
print("1️⃣7️⃣ all() - Check if all elements are True")
values = [True, True, True]
print(f"   {values}")
print(f"   all(list) = {all(values)}\n")

# 18. enumerate()
print("1️⃣8️⃣ enumerate() - Get index and value")
fruits = ['apple', 'banana', 'cherry']
print(f"   {fruits}")
print("   enumerate():")
for idx, fruit in enumerate(fruits):
    print(f"     {idx}: {fruit}\n")

# 19. zip()
print("1️⃣9️⃣ zip() - Combine lists")
names = ['Alice', 'Bob']
ages = [25, 30]
print(f"   names: {names}")
print(f"   ages: {ages}")
print("   zip():")
for name, age in zip(names, ages):
    print(f"     {name} - {age}\n")

# 20. in / not in
print("2️⃣0️⃣ in / not in - Membership testing")
my_list = [1, 2, 3, 4, 5]
print(f"   {my_list}")
print(f"   3 in list = {3 in my_list}")
print(f"   10 in list = {10 in my_list}\n")

# 21. Slicing
print("2️⃣1️⃣ Slicing - Get subsequence")
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"   {my_list}")
print(f"   list[2:5] = {my_list[2:5]}")
print(f"   list[::2] = {my_list[::2]}")
print(f"   list[::-1] = {my_list[::-1]}\n")

# 22. List comprehension
print("2️⃣2️⃣ List Comprehension - Create list efficiently")
squares = [x**2 for x in range(5)]
print(f"   [x**2 for x in range(5)] = {squares}")
evens = [x for x in range(10) if x % 2 == 0]
print(f"   [x for x in range(10) if x%2==0] = {evens}\n")

# 23. sorted()
print("2️⃣3️⃣ sorted() - Create sorted list (doesn't modify original)")
unsorted = [5, 2, 8, 1, 9]
sorted_list = sorted(unsorted)
print(f"   Original: {unsorted}")
print(f"   sorted(list): {sorted_list}\n")

print("\n")

# ============================================================
# PART 2: SET METHODS DEMONSTRATION
# ============================================================

print("=" * 70)
print("PART 2: SET - 15 METHODS")
print("=" * 70)
print()

# Create sets
my_set = {1, 2, 3, 4, 5}
print(f"Original set: {my_set}\n")

# 1. add()
print("1️⃣ add() - Add single element")
my_set.add(6)
print(f"   After add(6): {my_set}\n")

# 2. update()
print("2️⃣ update() - Add multiple elements")
my_set.update([7, 8, 9])
print(f"   After update([7,8,9]): {my_set}\n")

# 3. remove()
print("3️⃣ remove() - Remove element (error if missing)")
test_set = {1, 2, 3}
test_set.remove(2)
print(f"   {1, 2, 3} -> remove(2) -> {test_set}\n")

# 4. discard()
print("4️⃣ discard() - Remove element (no error if missing)")
test_set = {1, 2, 3}
test_set.discard(2)
print(f"   {1, 2, 3} -> discard(2) -> {test_set}")
test_set.discard(99)  # No error
print(f"   discard(99) -> {test_set} (no error)\n")

# 5. pop()
print("5️⃣ pop() - Remove and return arbitrary element")
test_set = {10, 20, 30}
element = test_set.pop()
print(f"   Removed: {element}")
print(f"   Remaining: {test_set}\n")

# 6. clear()
print("6️⃣ clear() - Remove all elements")
test_set = {1, 2, 3}
test_set.clear()
print(f"   After clear(): {test_set}\n")

# 7. union() or |
print("7️⃣ union() - Combine sets")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(f"   {set1} | {set2} = {result}\n")

# 8. intersection() or &
print("8️⃣ intersection() - Common elements")
result = set1.intersection(set2)
print(f"   {set1} & {set2} = {result}\n")

# 9. difference() or -
print("9️⃣ difference() - Elements in first but not second")
result = set1.difference(set2)
print(f"   {set1} - {set2} = {result}\n")

# 10. symmetric_difference() or ^
print("🔟 symmetric_difference() - Unique to each set")
result = set1.symmetric_difference(set2)
print(f"   {set1} ^ {set2} = {result}\n")

# 11. issubset() or <=
print("1️⃣1️⃣ issubset() - Check if subset")
subset = {1, 2}
superset = {1, 2, 3, 4}
print(f"   {subset} <= {superset} = {subset.issubset(superset)}\n")

# 12. issuperset() or >=
print("1️⃣2️⃣ issuperset() - Check if superset")
print(f"   {superset} >= {subset} = {superset.issuperset(subset)}\n")

# 13. isdisjoint()
print("1️⃣3️⃣ isdisjoint() - Check if no common elements")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(f"   {set1} isdisjoint {set2} = {set1.isdisjoint(set2)}")
set3 = {3, 4, 5}
print(f"   {set1} isdisjoint {set3} = {set1.isdisjoint(set3)}\n")

# 14. len()
print("1️⃣4️⃣ len() - Get number of elements")
my_set = {1, 2, 3, 4, 5}
print(f"   {my_set}")
print(f"   len(set) = {len(my_set)}\n")

# 15. in / not in
print("1️⃣5️⃣ in / not in - Membership testing (FAST!)")
my_set = {1, 2, 3, 4, 5}
print(f"   {my_set}")
print(f"   3 in set = {3 in my_set}")
print(f"   10 in set = {10 in my_set}\n")

print("\n")

# ============================================================
# PART 3: DICTIONARY METHODS DEMONSTRATION
# ============================================================

print("=" * 70)
print("PART 3: DICTIONARY (MAP) - 13 METHODS")
print("=" * 70)
print()

# Create a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(f"Original dict: {my_dict}\n")

# 1. keys()
print("1️⃣ keys() - Get all keys")
keys = my_dict.keys()
print(f"   keys(): {list(keys)}\n")

# 2. values()
print("2️⃣ values() - Get all values")
values = my_dict.values()
print(f"   values(): {list(values)}\n")

# 3. items()
print("3️⃣ items() - Get all key-value pairs")
items = my_dict.items()
print(f"   items(): {list(items)}\n")

# 4. get()
print("4️⃣ get() - Access with default value")
print(f"   get('name'): {my_dict.get('name')}")
print(f"   get('email'): {my_dict.get('email')}")
print(f"   get('email', 'unknown'): {my_dict.get('email', 'unknown')}\n")

# 5. pop()
print("5️⃣ pop() - Remove and return")
test_dict = {'a': 1, 'b': 2, 'c': 3}
value = test_dict.pop('b')
print(f"   pop('b') returned: {value}")
print(f"   Remaining: {test_dict}\n")

# 6. popitem()
print("6️⃣ popitem() - Remove and return last item")
test_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = test_dict.popitem()
print(f"   popitem() returned: ({key}, {value})")
print(f"   Remaining: {test_dict}\n")

# 7. clear()
print("7️⃣ clear() - Remove all items")
test_dict = {'a': 1, 'b': 2}
test_dict.clear()
print(f"   After clear(): {test_dict}\n")

# 8. update()
print("8️⃣ update() - Add/update items")
test_dict = {'a': 1, 'b': 2}
test_dict.update({'c': 3, 'd': 4})
print(f"   After update({{'c': 3, 'd': 4}}): {test_dict}\n")

# 9. setdefault()
print("9️⃣ setdefault() - Get with default set")
test_dict = {'a': 1}
val1 = test_dict.setdefault('a', 999)  # Key exists
val2 = test_dict.setdefault('b', 2)    # Key doesn't exist
print(f"   setdefault('a', 999): {val1}")
print(f"   setdefault('b', 2): {val2}")
print(f"   Dict after: {test_dict}\n")

# 10. copy()
print("🔟 copy() - Create shallow copy")
original = {'a': 1, 'b': 2}
copied = original.copy()
copied['a'] = 999
print(f"   Original: {original}")
print(f"   Copied: {copied}\n")

# 11. len()
print("1️⃣1️⃣ len() - Get number of key-value pairs")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"   {my_dict}")
print(f"   len(dict) = {len(my_dict)}\n")

# 12. in / not in
print("1️⃣2️⃣ in / not in - Check key existence")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"   {my_dict}")
print(f"   'a' in dict = {'a' in my_dict}")
print(f"   'z' in dict = {'z' in my_dict}")
print(f"   1 in dict = {1 in my_dict} (checks keys, not values!)\n")

# 13. dict.fromkeys()
print("1️⃣3️⃣ dict.fromkeys() - Create dict with default values")
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(f"   dict.fromkeys(['a','b','c'], 0): {new_dict}\n")

# BONUS: Iteration
print("BONUS: Iterate through dictionary")
test_dict = {'name': 'Bob', 'age': 30, 'city': 'London'}
print(f"   {test_dict}")
print("   Iteration with items():")
for key, value in test_dict.items():
    print(f"     {key}: {value}\n")

print("\n")

# ============================================================
# PART 4: QUICK COMPARISON
# ============================================================

print("=" * 70)
print("PART 4: QUICK COMPARISON")
print("=" * 70)
print()

print("📊 CHARACTERISTICS:")
print()
print("LIST: [1, 2, 3]")
print("  ✅ Ordered")
print("  ✅ Allows duplicates")
print("  ✅ Indexable")
print("  ✅ Mutable")
print("  📋 Use: When order matters and duplicates allowed\n")

print("SET: {1, 2, 3}")
print("  ❌ Unordered")
print("  ❌ No duplicates")
print("  ❌ Not indexable")
print("  ✅ Mutable")
print("  📋 Use: Fast lookup, unique elements\n")

print("DICTIONARY: {'a': 1, 'b': 2}")
print("  ✅ Ordered (3.7+)")
print("  ❌ No duplicate keys")
print("  ✅ Key-based access")
print("  ✅ Mutable")
print("  📋 Use: Key-value mapping, fast lookups\n")

print("⏱️ PERFORMANCE FOR LOOKUP:")
print("  List: O(n) - Need to search through all items")
print("  Set: O(1) - Fast hash-based lookup ⭐")
print("  Dict: O(1) - Fast hash-based lookup ⭐\n")

print("🎯 WHEN TO USE:")
print("  LIST: scores = [100, 95, 88]  # Ordered sequence")
print("  SET: unique_ids = {101, 102, 103}  # Remove duplicates")
print("  DICT: user = {'name': 'Alice', 'age': 25}  # Key-value pairs\n")

print("\n" + "=" * 70)
print("✅ ALL METHODS DEMONSTRATED!")
print("=" * 70)

