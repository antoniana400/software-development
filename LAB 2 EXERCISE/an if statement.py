# --- Year Comparison Program ---

# Set my birth year as a constant
MY_BIRTH_YEAR = 2006

# Get the user's birth year
year = int(input("Enter the year you were born: "))

# 1. Leap Year Check
if year % 4 == 0:
    print("You were born in a leap year")
else:
    print("You were not born in a leap year")

# 2. Age Comparison (The "Optional" part combined with the same year check)
if year < MY_BIRTH_YEAR:
    print("You're older than me")
elif year > MY_BIRTH_YEAR:
    print("You're younger than me")
else:
    # This runs if the year is not less than and not greater than, meaning it's equal
    print("You were born in the same year as me!")