#power of two , if there exists an integer x such that n == 2x
#solution 1

n = 1

if n <= 0:
    print(False)
else:
    while n % 2 == 0:
        n = n // 2

    if n == 1:
        print(True)
    else:
        print(False)

#solution 2
n = 1 
if n > 0 and (n & (n -1)) == 0:
    print(True)
else:
    print(False)

#Return all strings in words that are asubstring of another word

#solution 1 
words = ["mass", "as", "hero","superhero"]

result = []

for i in range(len(words)):
    for j in range(len(words)):
        if i != j and words[i] in words[j]:
           result.append(words[i])
           break
print(result)

#solution 2

class solution:
    def stringMatching(self, words):
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result        


