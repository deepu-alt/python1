#function with keywords
def fun(name, course, branch, per):
    print("hi I'am", name, course, branch, "with", per,"%")
fun(name="deepika", course= "b tech", branch="AIML", per=80)

# prime numbers without using functions
start = int(input("enter the starting number:"))
end = int(input("eneter the ending number:"))
print("prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
# function to check prime number
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# function to print prime numbers in range
def find_primes(start, end):
    for num in range(start, end + 1):
        if check_prime(num):
            print(num)

# input from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers are:")
find_primes(start, end)

# string
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