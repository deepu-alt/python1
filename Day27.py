# return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits.
#smallest number with all set bits 
def nextBeautifulNumber(n):
    # Precompute beautiful numbers (1, 3, 7, 15, 31, 63, 127, 255, 511, 1023)
    beautiful_numbers = [(1 << k) - 1 for k in range(1, 11)]  # Up to 10 bits

    for num in beautiful_numbers:
        if num >= n:
            return num

    return -1  # In case n is larger than the largest beautiful number we computed
n = int(input("Enter a number: "))
print(nextBeautifulNumber(n))  

#example 2
def smallestAllSetBits(n):
    # Start with the smallest beautiful number
    beautiful_number = 1

    while beautiful_number < n:
        beautiful_number = (beautiful_number << 1) | 1  # Shift left and add 1 to get the next beautiful number

    return beautiful_number
n = int(input("Enter a number: "))
print(smallestAllSetBits(n))

#prime numbers of set bits in binary representation

def countPrimeSetBits(self, left, right):
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        
    count = 0
    for num in range(left, right + 1):
        bits = bin(num).count('1')
        if bits in primes:
            count += 1
                
    return count
    
print(countPrimeSetBits(6, 10))  # Output: 4 (6, 7, 9, 10 have prime set bits)
