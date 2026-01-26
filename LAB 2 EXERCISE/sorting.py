print("Enter five different integers:")

a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
e = int(input("Number 5: "))

# Compare/swap against a
if b < a:
    a, b = b, a
if c < a:
    a, c = c, a
if d < a:
    a, d = d, a
if e < a:
    a, e = e, a

# Compare/swap against b
if c < b:
    b, c = c, b
if d < b:
    b, d = d, b
if e < b:
    b, e = e, b

# Compare/swap against c
if d < c:
    c, d = d, c
if e < c:
    c, e = e, c

# Compare/swap against d
if e < d:
    d, e = e, d

print("Numbers in increasing order:", a, b, c, d, e)
