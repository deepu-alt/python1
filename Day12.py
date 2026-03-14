#check if a number is positive
num = int(input("enter a number"))

result = num > 0
print("is the number positive?", result)

#even or odd
deepu = int(input("enter a number"))
if deepu % 2 == 0:
    print("the value is even")
else:
    print("the value is odd")

 #in boolean
deepu = int(input('enter a number'))
is_even = deepu % 2 == 0
print("is the number even?", is_even)    

#eligible to vote
age = int(input("enter a number"))

if age > 18:
    print("the person is eligible for vote")
else:
    print("the person is not eligible for vote")

#in boolean
age = int(input("enter a number"))

eligible = age >= 18
print("eligible to vote:", eligible)

#string contains vowels
text = input("enter a string")
vowels = "aeiouAEIOU"
result = any(ch in vowels for ch in text)
print("contains vowels:", result)

#logical operations
num = int(input("enter a number:"))
result = num > 10 and num < 50
print("number between 10 and 50:", result)

# list is empty
my_list = []

is_empty = not bool(my_list)

print("is list empty?", is_empty)

#function
def greater_than_100(num):
    return num > 100 

print(greater_than_100(150))
print(greater_than_100(50))