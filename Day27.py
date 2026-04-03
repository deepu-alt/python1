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

#prime numbers of set bits in binary representatio
# # Output: 4 (6, 7, 9, 10 have prime set bits)
def countPrimeSetBits(left, right):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_bits(x):
        return bin(x).count('1')

    count = 0
    for num in range(left, right + 1):
        if is_prime(count_bits(num)):
            count += 1

    return count

print(countPrimeSetBits(6, 10))  # ✅ Output: 4
#example2:

def countPrimeSetBits(left, right):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in range(left, right + 1):
        if is_prime(bin(num).count('1')):
            count += 1

    return count

# Correct way to call:

print(countPrimeSetBits(6, 10))  # ✅ Output: 4
# sum of values at indices with k set bits in their binary representation
def sumIndicesWithKSetBits(nums, k):
    def count_bits(x):
        return bin(x).count('1')
        
    total = 0
        
    for i in range(len(nums)):
        if count_bits(i) == k:
            total += nums[i]
        
    return total
    
print(sumIndicesWithKSetBits([1, 2, 3, 4, 5], 1))  # Output