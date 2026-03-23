#continue
n = int(input("enter a number"))

for i in range(1, n +1):
    if i % 2 == 0:
        print(i, True)
        continue
    
else:
    print(i, False)

#break
n  = int(input("enter a number"))

for i in range(1, n +1):
    if i % 2 == 0:
        print(i, True)
        continue
    
else:
    print(i, False)

