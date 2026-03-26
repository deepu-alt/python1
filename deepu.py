sentence = input("Enter a sentence: ")

words = sentence.split()

largest_word = ""
max_count = 0

for word in words:
    
    count = 0
    for ch in word:    
        count += 1

    if count > max_count:
        max_count = count
        largest_word = word

print("Largest word:", largest_word)

# palindrome
s = "A man, a plan, a canal: Panama"

cleaned = "".join(ch.lower() for ch in s if ch.isalnum())

print(cleaned == cleaned[::-1])
#dictionarys
s = "GeeksforGeeks"

count = {}   
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
result = []

for ch in count:
    if count[ch] > 1:
        result.append(ch)

print(result)

#write a python code to find  sum of all prime numbers below 100
def is_prime(n): #is_prime checks whether a number is prime or not 
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):# int(n**0.5) conevrts square root into an integer
        if n % i == 0:# it gives the reminder (ex:  case1: n=10 , i= 2 case2: n=10, i = 3)
            return False
        return True
total_sum = 0
for num in range(100):
    if is_prime(num):
        total_sum += num
        print("sum of prime numbers below 100:", total_sum)


#
sum_prime = 0
for num in range(2,100):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            sum_prime += num
            print(sum_prime)

       


#write a python code to print countdown from the given number to 0 using while loop


  