from typing import SupportsFloat, TypeAlias
from math import isfinite, sqrt

Vector2D: TypeAlias = tuple[float, float]

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

def vector_sum(vec1: Vector2D, vec2: Vector2D) -> Vector2D:
    x_new = vec1[0] + vec2[0]
    y_new = vec1[1] + vec2[1]
    return (x_new, y_new)

def vector_mag(vec: Vector2D) -> float:
    x, y = vec
    magnitude = sqrt((x**2) + (y**2))
    return magnitude

def unit_vector(vec: Vector2D) -> Vector2D:
    x, y = vec
    magnitude = vector_mag(vec)
    if magnitude <= 1e-6:
        raise ValueError("Vector magnitude is too small to normalize!")

    unit_y = y / magnitude
    unit_x = x / magnitude
    return (unit_x, unit_y)

def parse_vec(s: str, name: str) -> Vector2D:
    s = s.strip()
    dims = [d.strip() for d in s.split(",")]
    if len(dims) != 2:
        raise ValueError(f"{name} must be two comma-separated numbers!")
    x = _to_float(dims[0], name=f"{name} x")
    y = _to_float(dims[1], name=f"{name} y")
    return (x, y)

def main():
    print("Calculate an output vector from two inputs. Separate dimensions with a comma")

    while True:
        vec1_raw = input("> Vector 1: ").strip()
        if vec1_raw.lower() in {"q", "quit", ""}:
            break
        vec2_raw = input("> Vector 2: ").strip()
        if vec2_raw.lower() in {"q", "quit", ""}:
            break

        try:
            vec1 = parse_vec(vec1_raw, "Vector 1")
            vec2 = parse_vec(vec2_raw, "Vector 2")

            new_vec = vector_sum(vec1, vec2)
            new_mag = vector_mag(new_vec)
            new_unit_vec = unit_vector(new_vec)

            print(f"Sum vector: ({new_vec[0]:.2f}, {new_vec[1]:.2f})")
            print(f"Magnitude: {new_mag:.3f}")
            print(f"Unit vector: ({new_unit_vec[0]:.2f}, {new_unit_vec[1]:.2f})")
            break
        except NumericTypeError as e:
            print(f"Input error: {e}")
            continue
        except ValueError as e:
            print(f"Invalid value: {e}")
            continue


if __name__ == "__main__":
    main()