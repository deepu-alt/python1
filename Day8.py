#convert string to integer
num = input("enter the value:")
# type casting
num_int = int(num)

print(num_int)
print(type(num_int))
# covert string to integer

a = input("enter the value:")

b = float(a)

print(b)
print(type(b))

#convert flpat to integer

x = 9.8

y = int(x)

print(y)
print(type(y))

#covnvert integer to string
num = 100

s = str(num)

print(s)
print(type(s))

#add two numbers given as string
a = "15"
b = "20"

sum = int(a) + int(b)

print(sum)

#convert a number to string and integers

numbers = ["1", "2", "3", "4"]

result = []

for i in numbers:
    result.append(int(i))

print(result)

#convert tuple to list
t = (10, 20, 30)

l = list(t)

print(l)
print(type(l))