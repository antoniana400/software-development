# Get the initial price from the user
item_price = float(input("Enter the item price: "))

# Calculate tax as 20% of the price (Price / 100 * 20)
item_tax = (item_price/(20/100))

# Calculate the total price for a single item
total_price = item_price + item_tax

print("Tax on the item is", item_tax)
print("Total item price is", total_price)

# number of buys( quantity)
quantity = int(input("How many items do you want to buy? "))

# Calculate the final cost for all items
final_cost = total_price * quantity

print(f"The price for {quantity} items is {final_cost:.2f}")
#The code works perfectly when item price is entered
