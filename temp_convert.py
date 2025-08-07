from typing import SupportsFloat

class NumericTypeError(TypeError):
    """
    Raised when a parameter expects a numeric argument but 
    receives a non-numeric argument.
    """

def _to_float(x: SupportsFloat, *, name: str) -> float:
    try:
        if isinstance(x, bool):
            raise TypeError("Booleans are not accepted!")
        y = float(x)
    except Exception as e:
        raise NumericTypeError(f"{name.capitalize()} must be numeric; got {type(x).__name__}!") from e
    if not (y == y and abs(y) != float("inf")):
        raise ValueError(f"{name} must be finite; got {y}!")
    return y

def convert_temperature(temp: int | float | SupportsFloat, unit: str) -> float:
    in_temp = _to_float(temp, name="temperature")

    if unit == "C":
        new_temp = in_temp * 9/5 + 32
    elif unit == "F":
        new_temp = (in_temp - 32) * 5/9
    else:
        raise ValueError(f"{unit} is not a temperature unit!")
    
    return new_temp

def main():
    print("Celsius <---> Fahrenheit Converter")

    while True:
        usr_temp = input("Enter temperature: ").strip()
        usr_unit = input("Enter the current unit (C/F): ").strip().upper()

        try:
            converted = convert_temperature(usr_temp, usr_unit)

            if usr_unit == "C":
                print(f"Converted --> {converted:.2f}°F")
                break
            else:
                print(f"Converted --> {converted:.2f}°C")
                break
        except Exception as e:
            print(f"{e} Try again...")
            pass


if __name__ == "__main__":
    main()