from typing import SupportsFloat
from math import isfinite, hypot

type Vector2D = tuple[float, float]
type ScalarLike = SupportsFloat | str
type Vector2DLike = tuple[ScalarLike, ScalarLike]
EPSILON = 1e-6  # close to zero threshold

class NumericTypeError(TypeError):
    """Raised when a parameter expects a numeric argument but receives a non-numeric argument."""

def _to_float(usr_input: SupportsFloat | str, *, name: str) -> float:
    try:
        if isinstance(usr_input, bool):
            raise TypeError("Booleans are not accepted!")

        floating = float(usr_input)
    except (TypeError, ValueError) as e:
        raise NumericTypeError(f"{name.capitalize()} must be numeric; got {type(usr_input).__name__}!") from e

    if not isfinite(floating):
        raise ValueError(f"{name} must be finite; got {floating}!")

    return floating

def _coerce_vec(vec: Vector2DLike, name: str) -> Vector2D:
    if len(vec) != 2:
        raise ValueError(f"{name} must have length 2; got {len(vec)}")

    x = _to_float(vec[0], name=f"{name} x")
    y = _to_float(vec[1], name=f"{name} y")

    return (x, y)

def dot(vec1: Vector2DLike, vec2: Vector2DLike) -> float:
    v1 = _coerce_vec(vec1, "vec1")
    v2 = _coerce_vec(vec2, "vec2")

    return sum(v1i*v2i for v1i, v2i in zip(v1, v2))

def l2_norm(vec: Vector2DLike, *, name: str="vec") -> float:
    x, y = _coerce_vec(vec, name)
    
    return hypot(x, y)

# 
def unit_vector(vec: Vector2DLike, *, eps: float=1e-12, name: str="vec") -> Vector2D | None:
    x, y = _coerce_vec(vec, name)

    mag = hypot(x, y)
    if mag <= eps:
        return None
    return (x/mag, y/mag)