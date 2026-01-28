#box of X's of 7 wide and 5 high
for row in range(5):
    for col in range(7):
        print("X", end="")
    print()

#replacing x with numbers
print()

for row in range(5):
    for j in range(1, 8):
        print("{0:02}  ".format(j), end="")
    print()

print()

number = 1  # Independent counter

for row in range(5):
    for col in range(7):
        print("{0:02}  ".format(number), end="")
        number += 1
    print()
