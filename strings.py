# Multiline Strings
a = """
line1
line2
line3
line4
"""
print(a)


# Strings are Arrays
b = "Hello, World"
print(b[1])

print("")

# Looping Through a String
for b in "🍌banana":
    print(b)

print("")

# Slicing Strings
sliceStr = "Hello, World"
print(sliceStr[2:5])  # Slicing Strings
print(sliceStr[:5])  # Slice From the Start
print(sliceStr[2:])  # Slice To the End
print(sliceStr[-5:-2])  # Negative Indexing

print("")

# String Caseing
caseStr = "🐔Chicken 🍌Banana"
print(caseStr.upper())
print(caseStr.lower())

print("")

# Stripping Whitespace
spaceStr = "   Hello, World   "
print(spaceStr.strip())

print("")

# String replacement and splitting
analogicStr = "Needle,Sew"
print(analogicStr)
print(analogicStr.replace("N", "M"))
print(analogicStr.split(","))

print("")

# String Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

print("")

# Formatting Strings (F-Strings)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

print("")

# Formatting Numbers (F-Strings)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

print("")

txt = f"Price 💲{20 * 30}"
print(txt)
