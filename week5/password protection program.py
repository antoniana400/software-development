# Initialise attempts variable
attempts = 3

# Loop runs exactly three times (0, 1, 2)
for i in range(3):
    password = "password123"

    passwordInput = input("Enter your password: ")

    # Check if password is correct
    if passwordInput == password:
        print("Login successful. Welcome!")
        break  # Exit loop after successful login

    else:
        attempts -= 1

        if attempts == 0:
            print("You are locked out of the system.")
        else:
            print(f"Incorrect password. You have {attempts} attempt(s) left.")
