# create and access tuple
t = (1, 2, 3, 4, 5 )
print("first element:", t[0])
print("last element:", t[-1])

#tuple length
t = (1, 3, 4, 2, 6, 7)

print("length of tuple:", len(t))

#count occurrences

t = (1, 2, 3, 2, 4, 5, 2, 3, 4)
print("count of 2:", t.count(2))

#find index element

t = (13, 34, 54, 12, 23)

print("index of 12:", t.index(12))

#tuple slicing

t = (5, 10, 15, 20, 25)

print("sliced tuple:", t[1:4])

#convert tuple to list and modify

t = (1, 2, 3)

l = list(t)
l.append(4)

t = tuple(l)
print("update tuple:", t)

#unpacking tuple

t = (100, 200, 300)

a, b, c = t
print(a, b, c)

#swap two variables using tuple

a = 10
b = 20

a, b = b, a
print("a:", a, "b:", b)

#find maximum and minimum 
t = (8, 3, 15, 2, 10)

print("Max:", max(t))
print("Min:", min(t))

#nested tuple access

t = (1, (2, 3), (4, 5))

print("element:", t[1][1])

#remove duplicates from tuple

t = (1, 2, 2, 4, 3, 4, 3)

unique = tuple(set(t))
print("without duplicates:", unique)

# tuple concatenation

t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2
print("combine tuple:", t3)

#check elemnet exist
t = (2, 3, 4, 1, 5)

if 4 in t:
    print("element exist")
else:
    print("element not exist")

# tuple of string
t = ("apple", "banana", "kiwi", "watermelon")

longest = max(t, key=len)
print("longest word:", longest)

#tuple sorting

t = (2, 5, 7, 8, 1, 6)
sorted_t = tuple(sorted(t))
print("sorted tuple:", sorted_t)

#sum of elemnts
t = (1, 2, 3, 6, 7)
print("sum:", sum(t))

#reverse a tuple

t = (1, 3, 5, 6)
print("reversed tuple:", t[::-1])

# tuple with mixed data type

t = (1, "hello", 3.4, True)

print(t[1])
print(type(t[2]))

#find common elements between two tuples

t1 = (1, 2, 3, 4)
t2 = (1, 4, 5, 6)
common = tuple(set(t1)& set(t2))
print("common elements:", common)

#tuple frequency dictionary

t = (1, 2, 3, 2, 3, 4)

freq = {}
for i in t:
    freq[i] = freq.get(i, 0) + 1

    print(freq)

#example

t = ("apple", "banana", "apple", "orange", "banana", "apple")

freq = {}
for i in t:
    freq[i] = freq.get(i, 0) + 1
    print(freq)

#advance level

from collections import Counter

t = (1, 2, 2, 3, 3, 3)

freq = Counter(t)
print(freq)
