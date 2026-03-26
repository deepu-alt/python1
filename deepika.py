"""sum_primes = 0
for num in range(2,100):
    is_prime=True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            sum_primes += num
            print("sum of primes numbers below 100",sum_primes)
            """
num = int(input("enter a number:"))
count = 0
while num > 0 :
    print(num)
    num -= 1
    