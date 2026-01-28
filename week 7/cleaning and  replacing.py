text = input("Enter some text (with spaces if you like): ")

print("\nOriginal text:")
print(f"'{text}'")

# Trimming spaces
print("\nTrimmed text:")
print("strip():", f"'{text.strip()}'")
print("lstrip():", f"'{text.lstrip()}'")
print("rstrip():", f"'{text.rstrip()}'")

# Replace characters
replaced_text = text.replace("a", "@")
print("\nReplace 'a' with '@':")
print(replaced_text)

# Count letters
letter = input("\nEnter a letter to count: ")
print(f"The letter '{letter}' appears {text.count(letter)} time(s).")

# Check prefixes and suffixes
prefix = input("\nEnter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

print(f"Starts with '{prefix}':", text.startswith(prefix))
print(f"Ends with '{suffix}':", text.endswith(suffix))
