from typing import SupportsFloat
from math import isfinite, sqrt

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

def vector_sum(vec1: tuple[SupportsFloat, SupportsFloat],
               vec2: tuple[SupportsFloat, SupportsFloat]
) -> tuple[float, float]:
    x_new = vec1[0] + vec2[0]
    y_new = vec1[1] + vec2[1]
    return (x_new, y_new)

def vector_mag(vec: tuple[SupportsFloat, SupportsFloat]) -> float:
    x, y = vec
    magnitude = sqrt((x**2) + (y**2))
    return magnitude

def unit_vector(vec: tuple[SupportsFloat, SupportsFloat]
) -> tuple[SupportsFloat, SupportsFloat]:
    x, y = vec
    magnitude = vector_mag(vec)
    if magnitude <= 1e-6:
        print("Magnitude is null, double-check input vector...")
    else:
        unit_x = x / magnitude
        unit_y = y / magnitude
        return (unit_x, unit_y)

def main():
    print("Calculate an output vector from two inputs. Separate dimensions with a comma")

    while True:
        usr_in_1 = input("> Vector 1: ")
        usr_in_2 = input("> Vector 2: ")
    ...


if __name__ == "__main__":
    main()