def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Welcome to the Temperature Conversion Program!")

    temp = float(input("Enter the temperature: "))
    input_unit = input("Input unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    target_unit = input("Convert to (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    if input_unit == "celsius":
        if target_unit == "fahrenheit":
            result = celsius_to_fahrenheit(temp)
        elif target_unit == "kelvin":
            result = celsius_to_kelvin(temp)
        else:
            result = temp
    elif input_unit == "fahrenheit":
        if target_unit == "celsius":
            result = fahrenheit_to_celsius(temp)
        elif target_unit == "kelvin":
            result = fahrenheit_to_kelvin(temp)
        else:
            result = temp
    elif input_unit == "kelvin":
        if target_unit == "celsius":
            result = kelvin_to_celsius(temp)
        elif target_unit == "fahrenheit":
            result = kelvin_to_fahrenheit(temp)
        else:
            result = temp
    else:
        print("Invalid input unit. Please enter Celsius, Fahrenheit, or Kelvin.")
        return

    print(f"{temp}°{input_unit.capitalize()} = {result:.2f}°{target_unit.capitalize()}")

if __name__ == "__main__":
    main()