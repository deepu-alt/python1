num = int(input("enter a number: "))
sum = 0 

for i in range(1, num):
    if num % i == 0:
        sum += i
        if sum == num:
            print("perfect number")
        else:
            print("not a perfect number")
# Smallest digit
deepu = int(input("eneter a number:"))
smallest = 9
while deepu > 0:
    digit = deepu % 10
    if digit < smallest:
        smallest = digit
    deepu = deepu // 10
print("smallest digit:", smallest) 

#Product of digits
bindhu = int(input("enter a number:"))
product = 1
while bindhu > 0:
    digit = bindhu % 10
    product *= digit
    bindhu = bindhu // 10
print("product of digits:", product)  

# dictionary
sample_dict = {
    "name" : "kelly",
    "age" : 35,
    "salary" : 50000,
    "city": "new york"

}

keys = ["name", "salary"]
new_dict ={}

for key in keys:
    new_dict[key] = sample_dict[key]

print(new_dict)


# list
lst = [10, 20, 16, 23, 25, 16, 16, 10, 20]
k = 3
count_dict = {}
for num in lst:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for key, value in count_dict.items():
    if value == k:
        print("number appearing", k, "times:", key)
