numbers = [10, 7, 4, 9,12]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

#string contains vowels
def contains_vowels(s):
    vowels = "aieouAIEOU"
    for ch in s:
        if ch in vowels:
            return True
    return False
text = "python"
print(contains_vowels(text))

#fibonacci series

def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("enter number of terms:"))
fibonacci(n)


#arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))