from guards import Vector2D, Vector2DLike
from math import hypot, atan2, degrees
import guards as gd
import vectors2d as v2

def dot(vec1: Vector2DLike, vec2: Vector2DLike) -> float:
    x = gd._coerce_vec(vec1, "vec1")
    y = gd._coerce_vec(vec2, "vec2")

    return sum(x_i*y_i for x_i, y_i in zip(x, y))

def l2_norm(vec: Vector2DLike, *, name: str="vec") -> float:
    x, y = gd._coerce_vec(vec, name)
    
    return hypot(x, y)

def unit_vector(vec: Vector2DLike, *, eps: float=1e-12, name: str="vec") -> Vector2D | None:
    x, y = gd._coerce_vec(vec, name)

    mag = hypot(x, y)
    if mag <= eps:
        return None
    return (x/mag, y/mag)

def angle(vec1: Vector2DLike, vec2: Vector2DLike, *, eps: float | None=None) -> float:
    x1, y1 = gd._coerce_vec(vec1, "vec1")
    x2, y2 = gd._coerce_vec(vec2, "vec2")

    m1 = hypot(x1, y1)
    m2 = hypot(x2, y2)

    threshold = v2.EPSILON if eps is None else eps
    if m1 <= threshold or m2 <= threshold:
        raise ValueError(f"Vector magnitude is too small (<= {threshold}!)")

    dot_prod = x1*x2 + y1*y2
    cross = x1*y2 - y1*x2

    angle_rad = atan2(abs(cross), dot_prod)
    return degrees(angle_rad)
