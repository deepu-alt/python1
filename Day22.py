#remove duplicates
t = (1, 2, 2, 3, 4, 3)

unique = ()
for i in t:
    if i not in unique:
        unique = unique + (i,)

    print("unique:", unique)

#frequency count(manual)
t = (1, 2, 2, 3, 3, 3, 4)

freq = {}

for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#find second largest element

t = (10, 20, 5, 8, 20)

first = second = -9999

for i in t:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print("second largest:", second)

#check palindrome tuple

t = (1, 2, 3, 2, 1)

rev = ()

for i in t:
    rev = (i,) + rev
    
if t ==rev:
    print("palindrome")
else:
    print("not palindrome")

#
