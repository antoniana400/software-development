#I'm using cities.

cities = ["London", "Paris", "Tokyo", "New York", "Berlin", "Lagos", "Sydney", "Toronto"]

print("Current cities:", ", ".join(cities))

# Add an item
new_city = input("Enter a city to add: ")
cities.append(new_city)

# Remove an item
remove_city = input("Enter a city to remove: ")

if remove_city in cities:
    cities.remove(remove_city)
else:
    print("That city is not in the list.")

# Sort and display
cities.sort()
print("Updated city list:", ", ".join(cities))

#lists easily manipulate(modified) large data.
#A Turple is used when data provided cant be changed.
