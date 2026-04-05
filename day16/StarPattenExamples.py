
#range(start, stop, step)
#range(1, 6, 1) → forward (1 → 5)
#range(5, 0, -1) → backward (5 → 1)

#Right Triangle Pattern
rows = 5
for i in range(1, rows+1):
    print("*" * i)

print("---------------------------------------")

#Inverted Right Triangle

#start = rows → begins from rows (e.g., 5)
#stop = 0 → stops before 0
#step = -1 → decreases by 1 each time
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

print("---------------------------------------")

#Pyramid Pattern
rows = 5
for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

print("---------------------------------------")

#Inverted Pyramid
rows = 5
for i in range(rows):
    spaces = " " * i
    stars = "*" * (2 * (rows - i) - 1)
    print(spaces + stars)

print("---------------------------------------")

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

print("---------------------------------------")

#Square Pattern
rows = 8
for i in range(rows):
    print("*" * rows)

print("---------------------------------------")
#Hollow Square Pattern
rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * rows)
    else:
        print("#" + " " * (rows - 2) + "#")


print("-------------------------------------------")

#Left Triangle (Right-Aligned)
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)
