#reverse the string
s = input("enter a string:")
rev = s[:: -1]
print("reversed string:",rev)

#count the vowels in string
d = input("enter a string:")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("number of vowels in string:",count)

#find index of vowelss
c = input("enter a string:")
vowels = "aeiouAEIOU"
for i in range(len(c)):
    if c[i] in vowels:
        print("vowel:", c[i], "index:", i)

#palindrome string
a = input("enter a string:") 

if a == a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

#count the characters in string
b = input("enter a string:")

letters = digits = special = 0
for ch in b:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits +=1
    else:
        special += 1
        print("letters:",letters)
        print("digit:",digits)
        print("special characters:",special)

#convert uppercase to lowercase
e = input("enter a string:")
print("uppercase:", e.upper())
print("lowercase:",e.lower())

