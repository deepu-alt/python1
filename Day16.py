# occurrences of numbers in arr in unique
#solution 1
def uniqueOccurrences(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    counts = list(freq.values()) 
    return len(counts) == len(set(counts))
arr = [1, 2, 2, 1, 1, 3]
print(uniqueOccurrences(arr))

#solution 2
from collections import Counter

def uniqueOccurrences(arr):
    freq = Counter(arr)
    return len(freq.vqlues()) == len(set(freq.values()))
# solution 3
arr = [1, 2, 2, 1, 1, 3]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
count = list(freq.values())
if len(count) == len(set(count)):
    print(True)
else:
    print(False)

#solution 4
arr = [1, 2, 2, 1, 1, 3]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
count = list(freq.values())
if len(count) == len(set(count)):
    print(True)
else:
    print(False)

