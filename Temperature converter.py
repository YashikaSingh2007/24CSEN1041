def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


# Example usage
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Choose an option (1-6): "))
temp = float(input("Enter the temperature value: "))

if choice == 1:
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
elif choice == 2:
    print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
elif choice == 3:
    print(f"{temp}°C = {celsius_to_kelvin(temp)}K")
elif choice == 4:
    print(f"{temp}K = {kelvin_to_celsius(temp)}°C")
elif choice == 5:
    print(f"{temp}°F = {fahrenheit_to_kelvin(temp)}K")
elif choice == 6:
    print(f"{temp}K = {kelvin_to_fahrenheit(temp)}°F")
else:
    print("Invalid choice!")
