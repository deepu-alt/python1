#sum of list elemnts
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("sum:", total)

#reverse a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

#check elemnt exist in list
number = [10, 20, 30, 40, 50]

num = 30

if num in numbers:
    print("number exist in list ")
else:
    print("number not found")

#count occurrence of elemnt
number = [1, 2, 3, 2, 4, 2, 5]
count = number.count(2)
print("occurences:", count) 

#sort a list
number = [50, 10, 40, 20, 60]

number.sort()

print(number)

#Remove duplicate without using set
number = [1, 2, 2, 3, 4, 4, 5]

unique = []
for num in number:
    if num not in unique:
        unique.append(num)
print("list without duplicates:", unique)  

#find second largest element
numbers = [10, 20, 4, 45,99]

numbers = list(set(numbers))
numbers.sort()

print("second largest:", number[-2])

#rotate list (right rotation)
number = [1, 2, 3, 4, 5, 6]

k = 2 
k = k % len(number)
rotated = number[-k:] + number[: -k]

print("rotated list:",rotated)
