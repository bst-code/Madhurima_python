# 📚 COMPLETE GUIDE: LIST, SET, AND MAP (DICTIONARY)

**Last Updated:** April 5, 2026

---

## 📋 TABLE OF CONTENTS

1. [LIST - Complete Methods Guide](#list---complete-methods-guide)
2. [SET - Complete Methods Guide](#set---complete-methods-guide)
3. [MAP/DICTIONARY - Complete Methods Guide](#mapdictionary---complete-methods-guide)
4. [Comparison Table](#comparison-table)
5. [Quick Reference](#quick-reference)

---

# LIST - COMPLETE METHODS GUIDE

## Overview
A **List** is an ordered, mutable collection that allows duplicates.

```python
my_list = [1, 2, 3, 'hello', True, 3.14]
print(type(my_list))  # <class 'list'>
```

### Characteristics:
- ✅ **Ordered** - maintains insertion order
- ✅ **Mutable** - can be modified
- ✅ **Indexing** - supports indexing and slicing
- ✅ **Duplicates** - allows duplicate elements
- ✅ **Heterogeneous** - can store different data types
- ⏱️ **Time Complexity** - O(1) for access, O(n) for insertion/deletion

---

## LIST METHODS (23 Total)

### 1. **append(item)** - Add Single Element
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
```
- **Purpose:** Add element to END of list
- **Return:** None (modifies in-place)
- **Time Complexity:** O(1)
- **Example with strings:**
  ```python
  fruits = ['apple', 'banana']
  fruits.append('cherry')
  print(fruits)  # ['apple', 'banana', 'cherry']
  ```

---

### 2. **extend(iterable)** - Add Multiple Elements
```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
```
- **Purpose:** Add all elements from iterable to list
- **Return:** None (modifies in-place)
- **Time Complexity:** O(k) where k = length of iterable
- **Can extend with:**
  ```python
  list1 = [1, 2]
  list1.extend([3, 4])           # List
  list1.extend((5, 6))           # Tuple
  list1.extend('abc')            # String → [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']
  list1.extend({7, 8})           # Set
  ```

---

### 3. **insert(index, item)** - Insert at Position
```python
my_list = [1, 2, 4, 5]
my_list.insert(2, 3)
print(my_list)  # [1, 2, 3, 4, 5]
```
- **Purpose:** Insert element at specific position
- **Return:** None (modifies in-place)
- **Time Complexity:** O(n) - shifts elements
- **Examples:**
  ```python
  my_list = ['a', 'b', 'd']
  my_list.insert(2, 'c')  # ['a', 'b', 'c', 'd']
  my_list.insert(0, 'z')  # ['z', 'a', 'b', 'c', 'd']  (at beginning)
  my_list.insert(100, 'e') # Inserts at end if index too large
  ```

---

### 4. **remove(item)** - Remove by Value
```python
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 4]  (only first occurrence)
```
- **Purpose:** Remove FIRST occurrence of value
- **Return:** None (modifies in-place)
- **Time Complexity:** O(n)
- **Raises:** ValueError if item not found
- **Examples:**
  ```python
  fruits = ['apple', 'banana', 'apple']
  fruits.remove('apple')
  print(fruits)  # ['banana', 'apple']
  
  fruits.remove('cherry')  # ValueError: list.remove(x): x not in list
  ```

---

### 5. **pop(index=-1)** - Remove and Return by Index
```python
my_list = [1, 2, 3, 4, 5]
removed = my_list.pop()      # Remove last element
print(removed)  # 5
print(my_list)  # [1, 2, 3, 4]

removed = my_list.pop(0)     # Remove first element
print(removed)  # 1
print(my_list)  # [2, 3, 4]
```
- **Purpose:** Remove and return element at index
- **Return:** The removed element
- **Time Complexity:** O(n) for middle, O(1) for end
- **Default Index:** -1 (last element)
- **Raises:** IndexError if index out of range
- **Examples:**
  ```python
  stack = [10, 20, 30]
  print(stack.pop())      # 30 (like a stack - LIFO)
  print(stack)            # [10, 20]
  ```

---

### 6. **clear()** - Remove All Elements
```python
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # []
```
- **Purpose:** Remove all elements
- **Return:** None
- **Time Complexity:** O(n)
- **Example:**
  ```python
  data = ['a', 'b', 'c']
  data.clear()
  print(data)  # []
  print(len(data))  # 0
  ```

---

### 7. **index(item, start=0, end=len(list))** - Find Position
```python
my_list = [10, 20, 30, 20, 40]
pos = my_list.index(20)
print(pos)  # 1 (first occurrence)
```
- **Purpose:** Find FIRST occurrence of value
- **Return:** Index of first matching element
- **Time Complexity:** O(n)
- **Raises:** ValueError if item not found
- **With range:**
  ```python
  my_list = [1, 2, 3, 2, 4, 2]
  print(my_list.index(2))        # 1 (first occurrence)
  print(my_list.index(2, 2))     # 3 (from index 2 onwards)
  print(my_list.index(2, 4))     # 5 (from index 4 onwards)
  print(my_list.index(2, 0, 3))  # 1 (search between 0-3)
  ```

---

### 8. **count(item)** - Count Occurrences
```python
my_list = [1, 2, 2, 3, 2, 4]
count = my_list.count(2)
print(count)  # 3
```
- **Purpose:** Count occurrences of value
- **Return:** Number of times item appears
- **Time Complexity:** O(n)
- **Examples:**
  ```python
  grades = ['A', 'B', 'A', 'C', 'A']
  print(grades.count('A'))  # 3
  print(grades.count('D'))  # 0
  
  # Check for duplicates
  has_duplicates = any(my_list.count(x) > 1 for x in my_list)
  ```

---

### 9. **sort(key=None, reverse=False)** - Sort In-Place
```python
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)  # [1, 1, 3, 4, 5, 9]

my_list.sort(reverse=True)
print(my_list)  # [9, 5, 4, 3, 1, 1]
```
- **Purpose:** Sort list in-place
- **Return:** None (modifies in-place)
- **Time Complexity:** O(n log n)
- **Stable:** Yes (maintains relative order of equal elements)
- **Advanced examples:**
  ```python
  # Sort strings by length
  words = ['apple', 'dog', 'elephant']
  words.sort(key=len)
  print(words)  # ['dog', 'apple', 'elephant']
  
  # Sort tuples by second element
  pairs = [(1, 'z'), (2, 'a'), (3, 'b')]
  pairs.sort(key=lambda x: x[1])
  print(pairs)  # [(2, 'a'), (3, 'b'), (1, 'z')]
  
  # Custom sort function
  def custom_sort(x):
      return x % 10  # Sort by last digit
  
  numbers = [35, 12, 24, 16, 7]
  numbers.sort(key=custom_sort)
  print(numbers)  # [12, 24, 35, 16, 7]
  ```

---

### 10. **sorted(iterable, key=None, reverse=False)** - Create Sorted List
```python
my_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(my_list)
print(sorted_list)  # [1, 1, 3, 4, 5, 9]
print(my_list)      # [3, 1, 4, 1, 5, 9] (original unchanged)
```
- **Purpose:** Return NEW sorted list (doesn't modify original)
- **Return:** New list
- **Time Complexity:** O(n log n)
- **Works with any iterable:**
  ```python
  # Sort tuple
  t = (3, 1, 4)
  print(sorted(t))  # [1, 3, 4]
  
  # Sort string
  s = "hello"
  print(sorted(s))  # ['e', 'h', 'l', 'l', 'o']
  
  # Sort set
  st = {3, 1, 2}
  print(sorted(st))  # [1, 2, 3]
  ```

---

### 11. **reverse()** - Reverse In-Place
```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]
```
- **Purpose:** Reverse list in-place
- **Return:** None (modifies in-place)
- **Time Complexity:** O(n)
- **Alternative:** `my_list[::-1]` (creates new list)
  ```python
  original = [1, 2, 3]
  reversed_list = original[::-1]  # [3, 2, 1]
  print(original)  # [1, 2, 3] (unchanged)
  ```

---

### 12. **copy()** - Create Shallow Copy
```python
original = [1, 2, 3]
copied = original.copy()
copied[0] = 999
print(original)  # [1, 2, 3]
print(copied)    # [999, 2, 3]
```
- **Purpose:** Create shallow copy (independent copy)
- **Return:** New list
- **Time Complexity:** O(n)
- **Shallow vs Deep Copy:**
  ```python
  original = [[1, 2], [3, 4]]
  shallow = original.copy()
  deep = copy.deepcopy(original)  # Requires import copy
  
  shallow[0][0] = 999  # Changes original!
  print(original)  # [[999, 2], [3, 4]]
  
  deep[1][1] = 999  # Doesn't change original
  print(original)  # [[999, 2], [3, 4]] (no change from deep copy)
  ```

---

### 13. **len(list)** - Get Length
```python
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # 5
```
- **Purpose:** Get number of elements
- **Return:** Integer count
- **Time Complexity:** O(1)

---

### 14. **min(list)** - Find Minimum
```python
numbers = [3, 1, 4, 1, 5, 9]
minimum = min(numbers)
print(minimum)  # 1
```
- **Purpose:** Find smallest element
- **Return:** Minimum element
- **Time Complexity:** O(n)
- **With key parameter:**
  ```python
  words = ['apple', 'dog', 'elephant']
  shortest = min(words, key=len)
  print(shortest)  # 'dog'
  ```

---

### 15. **max(list)** - Find Maximum
```python
numbers = [3, 1, 4, 1, 5, 9]
maximum = max(numbers)
print(maximum)  # 9
```
- **Purpose:** Find largest element
- **Return:** Maximum element
- **Time Complexity:** O(n)

---

### 16. **sum(list, start=0)** - Sum All Elements
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 15

total = sum(numbers, 10)  # Start with 10
print(total)  # 25
```
- **Purpose:** Sum all numeric elements
- **Return:** Sum total
- **Time Complexity:** O(n)

---

### 17. **any(list)** - Check if Any True
```python
values = [False, False, True, False]
print(any(values))  # True

values = [0, 0, 0]
print(any(values))  # False
```
- **Purpose:** Check if any element is truthy
- **Return:** Boolean
- **Time Complexity:** O(n) worst case, O(1) best case
- **Examples:**
  ```python
  numbers = [0, 0, 5, 0]
  print(any(numbers))  # True (5 is truthy)
  
  words = ['', '', 'hello']
  print(any(words))  # True ('hello' is truthy)
  ```

---

### 18. **all(list)** - Check if All True
```python
values = [True, True, True]
print(all(values))  # True

values = [True, False, True]
print(all(values))  # False
```
- **Purpose:** Check if all elements are truthy
- **Return:** Boolean
- **Time Complexity:** O(n)
- **Examples:**
  ```python
  numbers = [1, 2, 3, 4, 5]
  print(all(numbers))  # True (all non-zero)
  
  numbers = [1, 2, 0, 4, 5]
  print(all(numbers))  # False (0 is falsy)
  ```

---

### 19. **enumerate(list)** - Get Index and Value
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```
- **Purpose:** Loop with index and value
- **Return:** Enumerate object
- **Time Complexity:** O(n)
- **With start parameter:**
  ```python
  items = ['a', 'b', 'c']
  for i, item in enumerate(items, start=1):
      print(f"{i}. {item}")
  # Output:
  # 1. a
  # 2. b
  # 3. c
  ```

---

### 20. **zip(list1, list2, ...)** - Combine Lists
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Output:
# Alice is 25
# Bob is 30
# Charlie is 35
```
- **Purpose:** Combine multiple iterables
- **Return:** Zip object
- **Time Complexity:** O(n)
- **With different lengths:**
  ```python
  a = [1, 2, 3, 4]
  b = ['a', 'b', 'c']
  
  print(list(zip(a, b)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
  # Stops at shortest iterable
  ```

---

### 21. **in / not in** - Membership Testing
```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # True
print(10 in my_list)     # False
print(10 not in my_list) # True
```
- **Purpose:** Check if element exists
- **Return:** Boolean
- **Time Complexity:** O(n)

---

### 22. **Slicing** - Get Subsequence
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[2:5])       # [2, 3, 4]      (index 2 to 4)
print(my_list[:3])        # [0, 1, 2]      (first 3)
print(my_list[5:])        # [5, 6, 7, 8, 9] (from index 5 to end)
print(my_list[::2])       # [0, 2, 4, 6, 8] (every 2nd element)
print(my_list[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
print(my_list[-3:])       # [7, 8, 9]      (last 3 elements)
```
- **Purpose:** Extract portions of list
- **Syntax:** `list[start:stop:step]`
- **Default Values:** `start=0, stop=len(list), step=1`

---

### 23. **Comprehension** - Create List Efficiently
```python
# Basic comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```
- **Purpose:** Create lists efficiently and readably
- **Time Complexity:** O(n)
- **More Pythonic:** Generally preferred over loops

---

## LIST OPERATIONS SUMMARY TABLE

| Method | Purpose | Time | Modifies | Returns |
|--------|---------|------|----------|---------|
| append() | Add single element | O(1) | Yes | None |
| extend() | Add multiple elements | O(k) | Yes | None |
| insert() | Insert at position | O(n) | Yes | None |
| remove() | Remove by value | O(n) | Yes | None |
| pop() | Remove by index | O(n) | Yes | Element |
| clear() | Remove all | O(n) | Yes | None |
| index() | Find position | O(n) | No | Index |
| count() | Count occurrences | O(n) | No | Count |
| sort() | Sort in-place | O(n log n) | Yes | None |
| reverse() | Reverse in-place | O(n) | Yes | None |
| copy() | Shallow copy | O(n) | No | New list |
| len() | Get length | O(1) | No | Count |
| min() | Find minimum | O(n) | No | Element |
| max() | Find maximum | O(n) | No | Element |

---

# SET - COMPLETE METHODS GUIDE

## Overview
A **Set** is an unordered, mutable collection with NO duplicates.

```python
my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>
```

### Characteristics:
- ❌ **Unordered** - no specific order
- ✅ **Mutable** - can be modified
- ❌ **No Indexing** - cannot access by index
- ❌ **No Duplicates** - automatically removes duplicates
- ✅ **Fast Lookup** - O(1) for membership testing
- ✅ **Hashable Elements** - only immutable types allowed

---

## SET METHODS (15 Total)

### 1. **add(element)** - Add Single Element
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

my_set.add(3)  # Duplicate - no change
print(my_set)  # {1, 2, 3, 4}
```
- **Purpose:** Add element to set
- **Return:** None (modifies in-place)
- **Time Complexity:** O(1) average
- **Note:** Duplicates are ignored (no error)

---

### 2. **update(*others)** or **|=** - Add Multiple Elements
```python
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # {1, 2, 3, 4, 5, 6}

my_set.update({7, 8}, [9])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```
- **Purpose:** Add all elements from iterables
- **Return:** None (modifies in-place)
- **Time Complexity:** O(k) where k = total elements added
- **Can update with multiple types:**
  ```python
  s = {1}
  s.update([2, 3])  # List
  s.update((4, 5))  # Tuple
  s.update({6, 7})  # Set
  print(s)  # {1, 2, 3, 4, 5, 6, 7}
  ```

---

### 3. **remove(element)** - Remove Element (Error if Missing)
```python
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  # {1, 2, 4}

my_set.remove(10)  # KeyError!
```
- **Purpose:** Remove element from set
- **Return:** None (modifies in-place)
- **Time Complexity:** O(1) average
- **Raises:** KeyError if element not found

---

### 4. **discard(element)** - Remove Element (No Error)
```python
my_set = {1, 2, 3, 4}
my_set.discard(3)
print(my_set)  # {1, 2, 4}

my_set.discard(10)  # No error!
print(my_set)  # {1, 2, 4}
```
- **Purpose:** Remove element (safe, no error if missing)
- **Return:** None (modifies in-place)
- **Time Complexity:** O(1) average
- **Difference from remove():** No error if element not found

---

### 5. **pop()** - Remove and Return Arbitrary Element
```python
my_set = {1, 2, 3, 4, 5}
element = my_set.pop()
print(element)  # Random element (e.g., 1)
print(my_set)   # Remaining elements
```
- **Purpose:** Remove and return arbitrary element
- **Return:** Removed element
- **Time Complexity:** O(1) average
- **Raises:** KeyError if set is empty
- **Note:** Unpredictable which element removed

---

### 6. **clear()** - Remove All Elements
```python
my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)  # set()
```
- **Purpose:** Remove all elements
- **Return:** None (modifies in-place)
- **Time Complexity:** O(n)

---

### 7. **len(set)** - Get Number of Elements
```python
my_set = {1, 2, 3, 4, 5}
size = len(my_set)
print(size)  # 5
```
- **Purpose:** Get number of elements
- **Return:** Integer count
- **Time Complexity:** O(1)

---

### 8. **in / not in** - Membership Testing
```python
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)      # True
print(10 in my_set)     # False
print(10 not in my_set) # True
```
- **Purpose:** Check if element exists
- **Return:** Boolean
- **Time Complexity:** O(1) average (key advantage over lists)

---

### 9. **union(*others)** or **|** - Combine Sets
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5}

# Using operator
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5}
```
- **Purpose:** Combine multiple sets (all unique elements)
- **Return:** New set
- **Time Complexity:** O(len(set1) + len(set2))
- **Multiple sets:**
  ```python
  s1 = {1, 2}
  s2 = {2, 3}
  s3 = {3, 4}
  
  result = s1.union(s2, s3)
  print(result)  # {1, 2, 3, 4}
  
  # Or using operator
  result = s1 | s2 | s3
  print(result)  # {1, 2, 3, 4}
  ```

---

### 10. **intersection(*others)** or **&** - Common Elements
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)
print(result)  # {3, 4}

# Using operator
result = set1 & set2
print(result)  # {3, 4}
```
- **Purpose:** Find common elements in all sets
- **Return:** New set
- **Time Complexity:** O(len(set1))
- **Multiple sets:**
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s3 = {2, 3, 5}
  
  result = s1.intersection(s2, s3)
  print(result)  # {2, 3}
  
  # Or using operator
  result = s1 & s2 & s3
  print(result)  # {2, 3}
  ```

---

### 11. **difference(*others)** or **-** - Elements in First But Not Others
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)
print(result)  # {1, 2}

# Using operator
result = set1 - set2
print(result)  # {1, 2}
```
- **Purpose:** Find elements in set1 NOT in other sets
- **Return:** New set
- **Time Complexity:** O(len(set1))
- **Multiple sets:**
  ```python
  s1 = {1, 2, 3, 4, 5}
  s2 = {2, 5}
  s3 = {4}
  
  result = s1.difference(s2, s3)
  print(result)  # {1, 3}
  
  # Or using operator
  result = s1 - s2 - s3
  print(result)  # {1, 3}
  ```

---

### 12. **symmetric_difference(other)** or **^** - Unique to Each Set
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)
print(result)  # {1, 2, 5, 6}  (in set1 or set2, but not both)

# Using operator
result = set1 ^ set2
print(result)  # {1, 2, 5, 6}
```
- **Purpose:** Find elements unique to each set
- **Return:** New set
- **Time Complexity:** O(len(set1) + len(set2))
- **Formula:** (A - B) ∪ (B - A)

---

### 13. **issubset(other)** or **<=** - Check if Subset
```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))  # True
print(set1 <= set2)         # True

# Strict subset
print(set1 < set2)  # True (not equal)
print(set2 < set2)  # False (same set)
```
- **Purpose:** Check if all elements of set1 are in set2
- **Return:** Boolean
- **Time Complexity:** O(len(set1))
- **Operators:**
  ```python
  s1 = {1, 2}
  s2 = {1, 2, 3}
  s3 = {1, 2}
  
  print(s1 <= s2)  # True (subset)
  print(s1 < s2)   # True (proper subset)
  print(s1 <= s3)  # True (equal sets)
  print(s1 < s3)   # False (not proper subset - they're equal)
  ```

---

### 14. **issuperset(other)** or **>=** - Check if Superset
```python
set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1.issuperset(set2))  # True
print(set1 >= set2)           # True

# Strict superset
print(set1 > set2)  # True
```
- **Purpose:** Check if set1 contains all elements of set2
- **Return:** Boolean
- **Time Complexity:** O(len(set2))
- **Operators:**
  ```python
  s1 = {1, 2, 3}
  s2 = {1, 2}
  
  print(s1 >= s2)  # True (superset)
  print(s1 > s2)   # True (proper superset)
  ```

---

### 15. **isdisjoint(other)** - Check if No Common Elements
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))  # True (no common elements)

set3 = {3, 4, 5}
print(set1.isdisjoint(set3))  # False (3 is common)
```
- **Purpose:** Check if sets have no common elements
- **Return:** Boolean
- **Time Complexity:** O(len(set1))

---

## IN-PLACE OPERATIONS (Modify Original Set)

### **intersection_update(*others)** or **&=**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.intersection_update(set2)
print(set1)  # {3, 4}  (modified in-place)

# Or using operator
set1 &= set2
```

### **difference_update(*others)** or **-=**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.difference_update(set2)
print(set1)  # {1, 2}  (modified in-place)

# Or using operator
set1 -= set2
```

### **symmetric_difference_update(other)** or **^=**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.symmetric_difference_update(set2)
print(set1)  # {1, 2, 5, 6}  (modified in-place)

# Or using operator
set1 ^= set2
```

---

## SET OPERATIONS SUMMARY TABLE

| Method | Purpose | Time | Modifies | Returns |
|--------|---------|------|----------|---------|
| add() | Add single element | O(1) | Yes | None |
| update() | Add multiple | O(k) | Yes | None |
| remove() | Remove (error) | O(1) | Yes | None |
| discard() | Remove (safe) | O(1) | Yes | None |
| pop() | Remove arbitrary | O(1) | Yes | Element |
| clear() | Remove all | O(n) | Yes | None |
| union() | Combine sets | O(n+m) | No | New set |
| intersection() | Common elements | O(n) | No | New set |
| difference() | Unique to first | O(n) | No | New set |
| symmetric_difference() | Unique to each | O(n+m) | No | New set |
| issubset() | Check subset | O(n) | No | Boolean |
| issuperset() | Check superset | O(m) | No | Boolean |
| isdisjoint() | Check no overlap | O(n) | No | Boolean |

---

# MAP/DICTIONARY - COMPLETE METHODS GUIDE

## Overview
A **Dictionary** (Map) is an unordered collection of key-value pairs.

```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(type(my_dict))  # <class 'dict'>
```

### Characteristics:
- ✅ **Key-Value Pairs** - maps keys to values
- ✅ **Mutable** - can be modified
- ❌ **No Indexing** - use keys to access values
- ✅ **Unique Keys** - no duplicate keys
- ✅ **Fast Lookup** - O(1) for key access
- ✅ **Ordered** (Python 3.7+) - maintains insertion order

---

## DICTIONARY METHODS (13 Total)

### 1. **keys()** - Get All Keys
```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
keys = my_dict.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

# Convert to list
keys_list = list(my_dict.keys())
print(keys_list)  # ['name', 'age', 'city']
```
- **Purpose:** Get all dictionary keys
- **Return:** dict_keys view object
- **Time Complexity:** O(n)
- **Modification during iteration:**
  ```python
  d = {'a': 1, 'b': 2, 'c': 3}
  for key in d.keys():
      print(key)
  # Output: a, b, c
  ```

---

### 2. **values()** - Get All Values
```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
values = my_dict.values()
print(values)  # dict_values(['Alice', 25, 'New York'])

# Convert to list
values_list = list(my_dict.values())
print(values_list)  # ['Alice', 25, 'New York']
```
- **Purpose:** Get all dictionary values
- **Return:** dict_values view object
- **Time Complexity:** O(n)

---

### 3. **items()** - Get All Key-Value Pairs
```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
items = my_dict.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# Loop through items
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: New York
```
- **Purpose:** Get all key-value pairs
- **Return:** dict_items view object (list of tuples)
- **Time Complexity:** O(n)

---

### 4. **get(key, default=None)** - Access with Default
```python
my_dict = {'name': 'Alice', 'age': 25}

print(my_dict.get('name'))      # 'Alice'
print(my_dict.get('city'))      # None (doesn't raise error)
print(my_dict.get('city', 'Unknown'))  # 'Unknown'
```
- **Purpose:** Safe key access with default value
- **Return:** Value if key exists, else default
- **Time Complexity:** O(1)
- **Advantage:** No KeyError like direct access
- **Examples:**
  ```python
  user = {'name': 'Bob'}
  
  # Using get() - safe
  email = user.get('email', 'no-email@example.com')
  print(email)  # 'no-email@example.com'
  
  # Using [] - unsafe
  # email = user['email']  # KeyError!
  ```

---

### 5. **pop(key, default=None)** - Remove and Return
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

value = my_dict.pop('b')
print(value)     # 2
print(my_dict)   # {'a': 1, 'c': 3}

# With default
value = my_dict.pop('z', 'not found')
print(value)  # 'not found'
```
- **Purpose:** Remove key and return its value
- **Return:** Value of removed key, else default
- **Time Complexity:** O(1)
- **Raises:** KeyError if key not found and no default
- **Examples:**
  ```python
  config = {'host': 'localhost', 'port': 8080}
  
  port = config.pop('port')
  print(port)    # 8080
  print(config)  # {'host': 'localhost'}
  ```

---

### 6. **popitem()** - Remove and Return Last Item
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

key, value = my_dict.popitem()
print(key, value)  # c 3 (last inserted)
print(my_dict)     # {'a': 1, 'b': 2}
```
- **Purpose:** Remove and return last key-value pair
- **Return:** Tuple of (key, value)
- **Time Complexity:** O(1)
- **Raises:** KeyError if dictionary is empty
- **Order:** Removes last inserted pair (Python 3.7+)

---

### 7. **clear()** - Remove All Items
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # {}
```
- **Purpose:** Remove all key-value pairs
- **Return:** None (modifies in-place)
- **Time Complexity:** O(n)

---

### 8. **update(other)** - Add/Update Items
```python
my_dict = {'a': 1, 'b': 2}
my_dict.update({'c': 3, 'd': 4})
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Update existing key
my_dict.update({'a': 999})
print(my_dict)  # {'a': 999, 'b': 2, 'c': 3, 'd': 4}
```
- **Purpose:** Add/update multiple key-value pairs
- **Return:** None (modifies in-place)
- **Time Complexity:** O(k) where k = items in other
- **Different ways to update:**
  ```python
  d = {'a': 1}
  
  # From dictionary
  d.update({'b': 2, 'c': 3})
  
  # From list of tuples
  d.update([('d', 4), ('e', 5)])
  
  # From keyword arguments
  d.update(f=6, g=7)
  
  print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
  ```

---

### 9. **setdefault(key, default=None)** - Get with Default Set
```python
my_dict = {'a': 1, 'b': 2}

# Key exists - returns existing value
value = my_dict.setdefault('a', 999)
print(value)     # 1
print(my_dict)   # {'a': 1, 'b': 2}

# Key doesn't exist - sets and returns default
value = my_dict.setdefault('c', 3)
print(value)     # 3
print(my_dict)   # {'a': 1, 'b': 2, 'c': 3}
```
- **Purpose:** Get value, or set and return default
- **Return:** Value if key exists, else default
- **Time Complexity:** O(1)
- **Use case:**
  ```python
  # Initialize dict with defaults if key missing
  scores = {'Alice': 95}
  
  scores.setdefault('Alice', 0)   # 95 (no change)
  scores.setdefault('Bob', 0)     # 0 (added)
  
  print(scores)  # {'Alice': 95, 'Bob': 0}
  ```

---

### 10. **copy()** - Create Shallow Copy
```python
original = {'a': 1, 'b': 2, 'c': [3, 4]}
copied = original.copy()

copied['a'] = 999
copied['c'].append(5)

print(original)  # {'a': 1, 'b': 2, 'c': [3, 4, 5]}
print(copied)    # {'a': 999, 'b': 2, 'c': [3, 4, 5]}
```
- **Purpose:** Create shallow copy
- **Return:** New dictionary
- **Time Complexity:** O(n)
- **Shallow vs Deep:**
  ```python
  original = {'a': 1, 'b': [2, 3]}
  shallow = original.copy()
  
  # Shallow copy: nested objects are not copied
  shallow['b'].append(4)
  print(original['b'])  # [2, 3, 4] - CHANGED!
  
  # Deep copy requires import
  import copy
  deep = copy.deepcopy(original)
  deep['b'].append(5)
  print(original['b'])  # [2, 3, 4] - NOT changed
  ```

---

### 11. **len(dict)** - Get Number of Key-Value Pairs
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
size = len(my_dict)
print(size)  # 3
```
- **Purpose:** Count number of key-value pairs
- **Return:** Integer count
- **Time Complexity:** O(1)

---

### 12. **in / not in** - Check Key Existence
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

print('a' in my_dict)       # True
print('z' in my_dict)       # False
print('z' not in my_dict)   # True

# Note: checks keys, not values
print(1 in my_dict)         # False (1 is a value, not key)
```
- **Purpose:** Check if key exists
- **Return:** Boolean
- **Time Complexity:** O(1)
- **Note:** Only checks keys by default
- **To check values:**
  ```python
  my_dict = {'a': 1, 'b': 2}
  
  print(2 in my_dict.values())  # True
  ```

---

### 13. **dict() Constructor** - Create Dictionary
```python
# From dictionary
d1 = dict({'a': 1, 'b': 2})
print(d1)  # {'a': 1, 'b': 2}

# From list of tuples
d2 = dict([('a', 1), ('b', 2)])
print(d2)  # {'a': 1, 'b': 2}

# From keyword arguments
d3 = dict(a=1, b=2, c=3)
print(d3)  # {'a': 1, 'b': 2, 'c': 3}

# From keys and default value
d4 = dict.fromkeys(['a', 'b', 'c'], 0)
print(d4)  # {'a': 0, 'b': 0, 'c': 0}
```
- **Purpose:** Create new dictionary
- **Return:** New dictionary
- **Time Complexity:** O(n)

---

## DICTIONARY COMPREHENSION

```python
# Basic comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From list of tuples
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
d = {k: v for k, v in pairs}
print(d)  # {1: 'a', 2: 'b', 3: 'c'}

# Swap keys and values
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {v: k for k, v in d1.items()}
print(d2)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## DICTIONARY OPERATIONS SUMMARY TABLE

| Method | Purpose | Time | Modifies | Returns |
|--------|---------|------|----------|---------|
| keys() | Get all keys | O(n) | No | dict_keys |
| values() | Get all values | O(n) | No | dict_values |
| items() | Get all pairs | O(n) | No | dict_items |
| get() | Safe access | O(1) | No | Value |
| pop() | Remove & return | O(1) | Yes | Value |
| popitem() | Remove last | O(1) | Yes | Tuple |
| clear() | Remove all | O(n) | Yes | None |
| update() | Add/update items | O(k) | Yes | None |
| setdefault() | Get with default | O(1) | Maybe | Value |
| copy() | Shallow copy | O(n) | No | New dict |
| len() | Get size | O(1) | No | Count |
| in | Check key | O(1) | No | Boolean |

---

# COMPARISON TABLE

## Quick Comparison of List, Set, and Dictionary

```
╔══════════════════╦════════════╦══════════╦═════════════════╗
║ Feature          ║ List       ║ Set      ║ Dictionary      ║
╠══════════════════╬════════════╬══════════╬═════════════════╣
║ Order            ║ Ordered ✅ ║ Unordered║ Ordered (3.7+) ✅║
║ Duplicates       ║ Yes        ║ No       ║ No (keys)       ║
║ Mutable          ║ Yes        ║ Yes      ║ Yes             ║
║ Indexing         ║ Yes        ║ No       ║ Key-based       ║
║ Lookup Speed     ║ O(n)       ║ O(1) ✅  ║ O(1) ✅          ║
║ Add Element      ║ O(1)       ║ O(1)     ║ O(1)            ║
║ Syntax           ║ [1,2,3]    ║ {1,2,3}  ║ {'a':1}         ║
║ Iteration        ║ Fast ✅    ║ Faster   ║ Fast            ║
║ Use Case         ║ Sequence   ║ Unique   ║ Mapping         ║
║ Methods          ║ 23         ║ 15       ║ 13              ║
╚══════════════════╩════════════╩══════════╩═════════════════╝
```

---

## When to Use What?

### **Use LIST when:**
- ✅ Order matters
- ✅ You need duplicates
- ✅ You need to access by index
- ✅ You need sequence operations (slicing, sorting)
- ✅ You need insertion/deletion at specific positions

**Examples:**
```python
scores = [100, 95, 88, 100]  # Grades with possible duplicates
students = ['Alice', 'Bob', 'Charlie']  # Ordered list of names
```

---

### **Use SET when:**
- ✅ You need unique elements only
- ✅ Order doesn't matter
- ✅ You need fast membership testing
- ✅ You need set operations (union, intersection, difference)
- ✅ You're removing duplicates from data

**Examples:**
```python
unique_ids = {101, 102, 103, 101}  # Auto removes duplicates
visited_cities = {'New York', 'London', 'Paris'}
```

---

### **Use DICTIONARY when:**
- ✅ You need to map keys to values
- ✅ You need fast lookups by key
- ✅ You're organizing structured data
- ✅ You need key-value associations
- ✅ You want named access instead of indices

**Examples:**
```python
user = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}
config = {'host': 'localhost', 'port': 8080, 'debug': True}
```

---

# QUICK REFERENCE

## Most Common Operations

### LIST
```python
my_list = [1, 2, 3]
my_list.append(4)           # Add element
my_list.remove(2)           # Remove by value
my_list.pop()               # Remove and return last
my_list.sort()              # Sort in-place
len(my_list)                # Get length
1 in my_list                # Check existence
```

### SET
```python
my_set = {1, 2, 3}
my_set.add(4)               # Add element
my_set.remove(2)            # Remove element
result = my_set.union(other_set)  # Combine sets
result = my_set.intersection(other_set)  # Common elements
1 in my_set                 # Check existence (fast!)
```

### DICTIONARY
```python
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3            # Add/update
value = my_dict.get('a')    # Safe access
my_dict.pop('b')            # Remove
for k, v in my_dict.items():  # Iterate
    pass
'a' in my_dict              # Check key existence
```

---

## Performance Cheat Sheet

```
┌─────────────────┬──────────┬──────────┬──────────┐
│ Operation       │ List     │ Set      │ Dict     │
├─────────────────┼──────────┼──────────┼──────────┤
│ Access          │ O(1)     │ N/A      │ O(1)     │
│ Search          │ O(n)     │ O(1) ⭐  │ O(1) ⭐  │
│ Insert          │ O(n)     │ O(1)     │ O(1)     │
│ Delete          │ O(n)     │ O(1)     │ O(1)     │
│ Iteration       │ O(n)     │ O(n)     │ O(n)     │
│ Union/Combine   │ O(n)     │ O(n+m)   │ O(k)     │
└─────────────────┴──────────┴──────────┴──────────┘
```

---

**Happy Learning! 🚀**

Practice these methods and you'll master Python's core data structures!

