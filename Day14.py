#create and print a list
numbers = [10, 20, 30, 40, 50]
print(numbers)
#access list elements
numbers = [5, 10, 15, 20, 25]

print("First element:", numbers[0])
print("Last element:", numbers[-1])

#add an element in list
fruits = ["apple", "banana", "mango"]

fruits.append("orange")

print(fruits)

#insert element at specific position
numbers = [1, 2, 4, 5]

numbers.insert(2, 3)

print(numbers)

#remove an element from list
colors = ["red", "blue", "green", "yellow"]

colors.remove("green")

print(colors)

#find length of list
numbers = [10, 20, 30, 40, 50]

print("Length of list:", len(numbers))

#find maximum and mim=nimum number
numbers = [15, 40, 5, 60, 25]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
