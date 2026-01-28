def clean(text):
    return text.strip().lower()


text = input("Enter some text (you can include multiple words or lines): ")

# Break text into parts
words = text.split()
lines = text.splitlines()

print("\nSplit into words:")
print(words)

print("\nSplit into lines:")
print(lines)

# Re-assemble text
rejoined_text = " | ".join(words)
print("\nRejoined text with separator:")
print(rejoined_text)

# Pad numbers
number_input = input("\nEnter a number to pad: ")

if number_input.isdigit():
    padded_number = number_input.zfill(5)
    print("Padded number:", padded_number)
else:
    print("Invalid number input.")

# Use clean() function
cleaned_text = clean(text)
print("\nCleaned text:")
print(cleaned_text)
