#Temperature in celcius
celcius = float(input("Enter the temperature in Celcius: "))

#converting to fahrenheit
fahrenheit = celcius * (9/5)+32
print(fahrenheit)

#Display format
print(f"{celcius}C = {fahrenheit:.2f}F")