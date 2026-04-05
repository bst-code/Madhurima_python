#Right Triangle Pattern

rows = 5
for i in range(1, rows):
    print("*" * i)

#Inverted Right Triangle

#start = rows → begins from rows (e.g., 5)
#stop = 0 → stops before 0
#step = -1 → decreases by 1 each time
rows = 5
for i in range(rows, 0, -1): #range(start, stop, step)
    print("*" * i)

#range(1, 6, 1) → forward (1 → 5)
#range(5, 0, -1) → backward (5 → 1)

#Pyramid Pattern
rows = 5
for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

#Inverted Pyramid

rows = 5
for i in range(rows):
    spaces = " " * i
    stars = "*" * (2 * (rows - i) - 1)
    print(spaces + stars)

#Diamond Pattern
rows = 5
# Upper part
for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# Lower part
for i in range(rows - 1):
    spaces = " " * (i + 1)
    stars = "*" * (2 * (rows - i - 1) - 1)
    print(spaces + stars)

#Square Pattern
rows = 5
for i in range(rows):
    print("*" * rows)

#Hollow Square Pattern
rows = 5

for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * rows)
    else:
        print("*" + " " * (rows - 2) + "*")

#Left Triangle (Right-Aligned)
rows = 5

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)