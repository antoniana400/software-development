print("Enter five different integers:")

a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
e = int(input("Number 5: "))

maximum = a  # assume first number is the largest

if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
if d > maximum:
    maximum = d
if e > maximum:
    maximum = e

print("The maximum number is:", maximum)
