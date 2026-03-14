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