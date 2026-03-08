#Fibonacci series
n = int(input("enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a,  end= " ")
    a, b = b, a + b

# count digits
num = int(input("enter a number: "))
count = 0 

while num > 0:
    num = num // 10
    count += 1

    print("total digits:", count)

#Largest digit in number 
deepu = int(input("enter a number:"))
largest = 0

while deepu > 0:
    digit = deepu % 10
    if digit > largest:
        largest = digit
        deepu = deepu // 10
        print("largest digit:", largest)

