run = True
while run:
    try:
        temp_celsius = input("Enter a temperature in Celsius:")
        temp_celsius = float(temp_celsius)
        temp_fahrenheit = (9 / 5) * temp_celsius + 32
        print(f"{temp_celsius:.2f} celsius is in {temp_fahrenheit:.2f}")
        break

    except ValueError:
        print("Please enter a valid floating point for the temperature.")

exit
