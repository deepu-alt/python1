#arithematic operation
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

#relational operations
x = 15
y = 20

print("x > y :", x > y)
print("x < y :", x < y)
print("x == y :", x == y)
print("x != y :", x != y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

#logical operations

num = 25

if num > 10 and num < 50:
    print("Number is between 10 and 50")
else:
    print("Number is not in the range")

#assignment operations
a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

#bitwise operations
a = 5
b = 3

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

#membership operations
numbers = [10, 20, 30, 40, 50]

num = 20

if num in numbers:
    print("Number is in the list")
else:
    print("Number is not in the list")

#identity operations
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True
print(a is c)     # False
print(a is not c) # True

#mixed operations
length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

