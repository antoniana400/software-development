#display 10x's in a row
for i in range(10):
    print("X", end="")
print()

#10*20 box of X's
print()

for row in range(10):
    for col in range(20):
        print("X", end="")
    print()

#10 high * 5 wide box
print()

for row in range(10):
    for col in range(5):
        print("X", end="")
    print()

#T shape boxes.
print()

# Top horizontal bar (4 high, 15 wide)
for row in range(4):
    for col in range(15):
        print("X", end="")
    print()

# Vertical bar (10 high, 5 wide, shifted right)
for row in range(10):
    print(" " * 5, end="")
    for col in range(5):
        print("X", end="")
    print()

print()


#L shape (2 boxes:10*5 and 4*15)
# Tall vertical part (10 high, 5 wide)
for row in range(10):
    for col in range(5):
        print("X", end="")
    print()

# Bottom horizontal part (4 high, 15 wide)
for row in range(4):
    for col in range(15):
        print("X", end="")
    print()
