# Reverse a number
num = int(input ("enter a number:"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("reversed number:", rev)

# Palindrome number
deepu = int(input("enter a number:"))
temp = deepu 
rev = 0
while deepu > 0:
    digit = deepu % 10
    rev = rev * 10 +digit
    deepu = deepu // 10

if temp == rev:
    print("Palindrome")
else:
    print("not Palindrome")    


#Armstrong number
D = int(input("enter a number: "))
temp = D
sum = 0

while D > 0:
    digit = D % 10
    sum += digit ** 3
    D = D // 10

if sum == temp:
    print("Armstrong number")
else:
    print("not Armstrong")  

  