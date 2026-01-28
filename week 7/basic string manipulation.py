word = input("Enter a word: ")

print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("Capitalized:", word.capitalize())
print("Title case:", word.title())
print("Swap case:", word.swapcase())
print("Reversed:", word[::-1])
print("Number of characters:", len(word))

if 'a' in word:
    print("The letter 'a' is in the word.")
else:
    print("The letter 'a' is not in the word.")
