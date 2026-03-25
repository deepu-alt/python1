#if statements
age = 18
if age >= 18:
    print("you are eligible to vote")

#if-else statements
num = 5
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# if-elif-else statement
marks = 75
if marks >= 90:
    print("grade A")
elif marks >= 60:
    print("grade B")
else:
    print("gate C")

#nested if
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive Even")

# important operators
#coparison: ==, !=, >, <, >=, <=
# logical: and, or not 
# practice problems
# check positive / negative / zero 
num = int(input("Enter a number:"))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

#check leap year 

year = int(input("Enter year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")



