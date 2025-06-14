# Number of rows
rows = 5

# 1. Lower Triangular Pattern
print("Lower Triangular Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Upper Triangular Pattern
print("\nUpper Triangular Pattern:")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 3. Pyramid Pattern
print("\nPyramid Pattern:")
for i in range(1, rows + 1):
    # print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # print stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()