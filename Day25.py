# a set is a collection of unique (no duplicates) and unordered elements
#creating a set
from Day17 import solution


s = {1, 2, 3, 4}
b = set([4, 5, 6])
print(b)

# find duplicates elements
lst = [1, 2, 3, 4, 3,4 , 2, 43, 4 ]

seen = set() # it creates empty set to store seen element // seen is a variable name we can assign any variable near seen

duplicates = set()# it is used to store repeated(duplicates) values

for item in lst:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicates:", duplicates)

# removes duplicates from list
unique_list = list(set(lst))

print("unique list:", unique_list)

seen = set()
result = []
for num in lst:
    if num not in seen:
        seen.add(num)
        result.append(num)
        print(result)

#check common elements 
a = [1, 2, 3, 4, 6]
b = [5, 2, 9, 0]
print(len(set(a)&set(b)) >0)
#print common elements
common_elements = set(a) & set(b)
print("common elements:", common_elements)

#symmetric difference 
sym_diff = set(a) ^ set(b)
print("symetric difference:", sym_diff)

#pair with given sum
lst = [1, 2, 3, 5, 6, 4]
target = 6
seen = set()
for num in lst:
    if target - num in seen:
        print((num, target -num))
    seen. add(num)

#longest substring without repeating characters
s = "abcabcbb"

char_set = set()
left = 0
max_length = 0

for right in range(len(s)):
    print("Checking:", s[right])

    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

    print("Window:", s[left:right+1], "Length:", max_length)

print("Final:", max_length)
#example 2
s = "abcabcbb"

char_set = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)

#check the consecutive numbers

lst = [3, 4, 5, 6, 7]
if max(lst) - min(lst) +1 == len(set(lst)):
    print(True)
else:
    print(False)

#gratesr common devisor
nums = [2, 5, 6, 9, 10]

smallest = min(nums)
largest = max(nums)

# Euclidean Algorithm
while largest % smallest != 0:
    largest, smallest = smallest, largest % smallest

print(smallest)   # Output: 2    

# intersection of three lists
a = [1,2,3]
b = [2,3,4]
c = [2,3,5]

result = set(a) & set(b) & set(c)
print(result)

#smallest missing positive number
lst = [1,2,0]

s = set(lst)
i = 1

while True:
    if i not in s:
        print(i)
        break
    i += 1