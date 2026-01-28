# #practice 1(integer declaration)
fileCount = 0
fileCount += 1
fileSize = 1000
print(f"The number of files is \033[31m{fileCount}\033[0m, the file size is [\033[31m{fileSize}\033[0m].")

#practice 2(age determination)
age_input = input("Please enter your age: ")

if age_input.isdigit():
    age = int(age_input)

    if age < 18:
        print("You are a child.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a pensioner.")
else:
    print("Invalid input. Please enter a whole number for your age.")

#practice 3(guessing game)
import random

# Generating a random number between 1 and 100
randomNumber = random.randint(1, 100)

while True:
    guess_input = input("Enter your guess (1–100): ")

    # Input validation to prevent errors
    if not guess_input.isdigit():
        print("Invalid input. Please enter a whole number.")
        continue

    guess = int(guess_input)

    if guess < randomNumber:
        print("Incorrect. The correct number is higher.")
    elif guess > randomNumber:
        print("Incorrect. The correct number is lower.")
    else:
        print("Correct! You guessed the number.")
        break

#Practice 4( 12 times -table)
for i in range(1, 13):
    print(f"12 x {i} = {12 * i}")

#Practice 5

print("Menu")
print("1. Start game")
print("2. Load game")
print("3. Settings")
print("4. Help")
print("5. Exit")

while True:
    choice_input = input("Please enter your choice (1–5): ")

    # Check if input is a number
    if not choice_input.isdigit():
        print("Error: Please enter a number between 1 and 5.")
        continue

    choice = int(choice_input)

    # Check if number is in valid range
    if choice < 1 or choice > 5:
        print("Error: Choice must be between 1 and 5.")
        continue

    break  # Valid input entered

print(f"You selected option {choice}.")

#shapes
height_input = input("Enter the height of the shapes: ")

if not height_input.isdigit():
    print("Invalid input. Please enter a whole number.")
else:
    height = int(height_input)


    # Shape 1: Outline right-angled triangle

    print("\nShape 1:\n")

    for row in range(1, height + 1):
        for col in range(1, row + 1):
            if col == 1 or col == row or row == height:
                print("X", end="")
            else:
                print(" ", end="")
        print()


    # Shape 2: Outline pyramid

    print("\nShape 2:\n")

    for row in range(height):
        # Leading spaces
        for space in range(height - row - 1):
            print(" ", end="")

        # Xs and spaces
        for col in range(2 * row + 1):
            if col == 0 or col == 2 * row or row == height - 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()

    # =====================
    # Shape 3: Difficult shape (1 outer + 3 inner loops)
    # =====================
    print("\nShape 3:\n")

    for row in range(height):
        # Left padding
        for space in range(row):
            print(" ", end="")

        # Left block
        for x in range(4):
            print("X", end="")

        # Middle gap
        for space in range((height - row - 1) * 2):
            print(" ", end="")

        # Right block
        for x in range(4):
            print("X", end="")

        print()




