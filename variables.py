# x = 5
# y = "John"
# print(x)
# print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# x = 4
# x = "Sally"
# print(x)

# Casting
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

print("")

# Python allows you to assign values to multiple variables in one line:
x, y, z = "🍊Orange", "🍌Banana", "🍒Cherry"
print("Assign values to multiple variables:")
print(x)
print(y)
print(z)

print("")

# And you can assign the same value to multiple variables in one line:
x = y = z = "🍊Orange"
print("One Value to Multiple Variables:")
print(x)
print(y)
print(z)

print("")

# Unpack a collection (unpacking)
fruits = ["🍎Apple", "🍌Banana", "🍒Cherry"]
print("Unpack a collection:")
x, y, z = fruits
print(x)
print(y)
print(z)
