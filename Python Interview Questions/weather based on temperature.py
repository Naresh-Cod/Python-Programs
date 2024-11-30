
temperature = float(input("Enter the temperature (in °C): "))
humidity = float(input("Enter the humidity (in %): "))

if temperature >= 30 and humidity >= 90:
    print("Weather Condition: Hot and humid")
elif temperature >= 30 and humidity < 90:
    print("Weather Condition: Hot")
elif temperature < 30 and humidity >= 90:
    print("Weather Condition: Cool and humid")
elif temperature < 30 and humidity < 90:
    print("Weather Condition: Cool")
else:
    print("Weather Condition: Invalid input")
