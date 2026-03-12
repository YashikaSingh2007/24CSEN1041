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


OUTPUT:
Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Choose an option (1-6): 3
Enter the temperature value: 37
37.0°C = 310.15K


Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Choose an option (1-6): 1
Enter the temperature value: 40
40.0°C = 104.0°F


Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Choose an option (1-6): 2
Enter the temperature value: 109
109.0°F = 42.77777777777778°C


Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Choose an option (1-6): 4
Enter the temperature value: 203
203.0K = -70.14999999999998°C


Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Choose an option (1-6): 5
Enter the temperature value: 300
300.0°F = 422.0388888888889K


Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Choose an option (1-6): 6
Enter the temperature value: 53
53.0K = -364.27°F


