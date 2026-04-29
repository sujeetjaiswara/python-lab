a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If
num1 = 5
num2 = 2
if num1 > num2:
    print("num1 is greater than num2")

# Assign a Value With If ... Else
result = num1 if num1 > num2 else num2
print(result)
