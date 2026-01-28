# Clue 1: Basic Function

def greetUser():
    print("Welcome to the Python treasure hunt!")

# Clue 2: Function with Return Value

def calculateSum(a, b):
    return a + b

# Clue 3: Default Parameters

def createUserProfile(userName, userAge=25, userCountry="Unknown"):
    return {
        "name": userName,
        "age": userAge,
        "country": userCountry
    }

# Clue 4: Variable-Length Arguments (*args)

def calculateTotalSum(*numbers):
    return sum(numbers)

# Clue 5: Lambda Function

squareNumber = lambda x: x * x

# Clue 6: Recursive Function


def calculateFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculateFactorial(n - 1)

# Clue 7: Generator Function

def numberSequenceGenerator(limit):
    for i in range(limit):
        yield i

# FINAL CHALLENGE


def main():
    # 1. Greet the user
    greetUser()
    print()

    # 2. Calculate sum of 15 and 25
    total = calculateSum(15, 25)
    print("Sum of 15 and 25:", total)
    print()

    # 3. Create user profile
    userProfile = createUserProfile("Alex", 5, "UK")
    print("User Profile:", userProfile)
    print()

    # 4. Calculate factorial of user's age
    ageFactorial = calculateFactorial(userProfile["age"])
    print("Factorial of user's age:", ageFactorial)
    print()

    # 5. Calculate total sum using *args
    numbersTotal = calculateTotalSum(1, 2, 3, 4, 5)
    print("Total sum of numbers:", numbersTotal)
    print()

    # 6. Lambda function example
    print("Square of 4:", squareNumber(4))
    print()

    # 7. Generator example
    print("Generated number sequence up to 5:")
    for num in numberSequenceGenerator(5):
        print(num, end=" ")
    print("\n")

    # Final Treasure Message
    print("🎉 Congratulations! You’ve found the Python treasure! 🎉")


# Run the final challenge
main()
