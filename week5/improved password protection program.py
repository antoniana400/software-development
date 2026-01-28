# Correct password
password = "password123"

# Loop counting backward from 3 attempts to 1
for attempts_left in range(3, 0, -1):
    passwordInput = input("Enter your password: ")

    if passwordInput == password:
        print("Login successful. Welcome!")
        break
    else:
        if attempts_left == 1:
            print("You are locked out of the system. Please contact the admin.")
        else:
            print(f"Incorrect password. You have {attempts_left - 1} attempt(s) left.")
