from typing import SupportsFloat
from math import isfinite

class NumericTypeError(TypeError):
    """Raised when a parameter expects a numeric argument but receives a non-numeric argument."""

def _to_float(x: SupportsFloat | str, *, name: str) -> float:
    try:
        if isinstance(x, bool):
            raise TypeError("Booleans are not accepted!")
        
        y = float(x)
    except (TypeError, ValueError) as e:
        raise NumericTypeError(f"{name.capitalize()} must be numeric; got {type(x).__name__}!") from e
    
    if not isfinite(y):
        raise ValueError(f"{name} must be finite; got {y}!")
    
    return y

def convert_temperature(temp: SupportsFloat | str, unit: str) -> tuple[float, str]:
    in_temp = _to_float(temp, name="temperature")
    unit = unit.strip().upper()

    match unit:
        case "C": 
            return in_temp * 9/5 + 32, "F"
        case "F": 
            return (in_temp - 32) * 5/9, "C"
        case _: 
            raise ValueError(f"{unit!r} is not a temperature unit!")

def main():
    print("Celsius <---> Fahrenheit Converter")

    while True:
        usr_temp = input("> Enter temperature: ").strip()
        usr_unit = input("> Enter the current unit (C/F): ")

        try:
            converted, target = convert_temperature(usr_temp, usr_unit)
        except (NumericTypeError, ValueError) as e:
            print(f"{e} Try again...")
            continue

        print(f"Converted --> {converted:.2f}°{target}")
        break


if __name__ == "__main__":
    main()