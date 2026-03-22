#Maximum element in tuple
t = (3, 4, 2, 5, 6)

max_val = t[0]
for i in t:
    if i > max_val:
        max_val = i

        print("maximum:", max_val)

# Minimum element in tuple
t = (3, 4, 5, 7, 8, 6)

min_val = t[0]

for i in t:
    if i < min_val:
        min_val = i

        print("minimum :", min_val)

#sum of elements
t= (3, 7, 4, 6, 2, 9)

total = 0
for i in t:
    total += i

    print("sum:", total)

#count even and odd numbers

t = (1, 3, 6, 4, 7, 9, 8)

even = 0
odd = 0

for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

        print("even:", even)
        print("odd:", odd)

#reverse a tuple(without slicing)

t = (1, 3, 4, 5, 6)

rev = ()

for i in t:
    rev = (i,) + rev

print("reversed:", rev)

