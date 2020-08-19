# This is for indexing and slicing| Use indexing/slicing to print "we win"
#         01234567890123
parrot = "Norwegian Blue"

# This is a STEP using slice

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

print()

# Slicing with negative numbers

print(parrot[0:6])
print(parrot[-14:-8])

print(parrot[-4:-2])


print()


# This is the slicing

print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])

print()

# This is indexing
print(parrot[3])
print(parrot[4])

print()

print(parrot[3])
print(parrot[6])
print(parrot[8])
