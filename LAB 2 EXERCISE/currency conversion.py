pounds = float(input("Enter amount in pounds (£): "))
dollars = pounds * 1.5
print("Amount in dollars: $", dollars)
#conversion
choice = int(input("Type 1 to convert £ to $, or type 2 to convert $ to £: "))
rate = float(input("Enter the exchange rate ($ per £): "))

if choice == 1:
    amount = float(input("Enter amount in pounds (£): "))
    result = amount * rate
    print("Amount in dollars: $", result)
else:
    amount = float(input("Enter amount in dollars ($): "))
    result = amount / rate
    print("Amount in pounds (£): £", result)

#after choice
choice = int(input("Type 1 to convert £ to $, or type 2 to convert $ to £: "))
rate = float(input("Enter the exchange rate ($ per £): "))
amount = float(input("Enter the amount to convert: "))

if choice == 1:
    result = amount * rate
else:
    result = amount / rate

print("Converted amount:", result)
