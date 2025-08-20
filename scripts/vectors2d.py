from typing import SupportsFloat
from math import isfinite, sqrt

type Vector2D = tuple[float, float]
type ScalarLike = SupportsFloat | str
type Vector2DLike = tuple[ScalarLike, ScalarLike]
EPSILON = 1e-6  # close to zero threshold

class NumericTypeError(TypeError):
    """Raised when a parameter expects a numeric argument but receives a non-numeric argument."""

def _to_float(input: SupportsFloat | str, *, name: str) -> float:
    try:
        if isinstance(input, bool):
            raise TypeError("Booleans are not accepted!")
        
        floating = float(input)
    except (TypeError, ValueError) as e:
        raise NumericTypeError(f"{name.capitalize()} must be numeric; got {type(input).__name__}!") from e
    
    if not isfinite(floating):
        raise ValueError(f"{name} must be finite; got {floating}!")
    
    return floating

def _coerce_vec(vec: Vector2DLike, name: str) -> Vector2D:
    x = _to_float(vec[0], name=f"{name} x")
    y = _to_float(vec[1], name=f"{name} y")
    
    return (x, y)

def vector_sum(vec1: Vector2DLike, vec2: Vector2DLike) -> Vector2D:
    v1 = _coerce_vec(vec1, "vec1")
    v2 = _coerce_vec(vec2, "vec2")
    
    return (v1[0] + v2[0], v1[1] + v2[1])

def vector_mag(vec: Vector2DLike, *, name: str="vec") -> float:
    x, y = _coerce_vec(vec, name)
    
    return sqrt((x**2) + (y**2))

def unit_vector(vec: Vector2DLike, *, name: str="vec") -> Vector2D:
    x, y = _coerce_vec(vec, name)
    mag = sqrt(x**2 + y**2)
    if mag <= EPSILON:
        raise ValueError(f"{name} magnitude is too small to normalize (<= {EPSILON})!")

    return (x/mag, y/mag)

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
            selection = input(f"Run again? [y/n]: ")
            break
        except NumericTypeError as e:
            print(f"Input error: {e}")
            continue
        except ValueError as e:
            print(f"Invalid value: {e}")
            continue


if __name__ == "__main__":
    main()