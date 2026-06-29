def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

# Input from user
celsius = float(input("Enter temperature in Celsius: "))

# Function call
fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)