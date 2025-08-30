from guards import Vector2D, Vector2DLike
from math import hypot, atan2, degrees
import guards as gd
import vectors2d as v2

def dot_2d(vec1: Vector2DLike, vec2: Vector2DLike) -> float:
    x1, y1 = gd.coerce_vec2d(vec1, "vec1")
    x2, y2 = gd.coerce_vec2d(vec2, "vec2")

    return x1*x2 + y1*y2

def cross_2d(vec1: Vector2DLike, vec2: Vector2DLike) -> float:
    x1, y1 = gd.coerce_vec2d(vec1, "vec1")
    x2, y2 = gd.coerce_vec2d(vec2, "vec2")

    return x1*y2 - y1*x2

def l2_norm(vec: Vector2DLike, *, name: str="vec") -> float:
    x, y = gd.coerce_vec2d(vec, name)
    
    return hypot(x, y)

def unit_vector(vec: Vector2DLike, *, eps: float=1e-12, name: str="vec") -> Vector2D | None:
    x, y = gd.coerce_vec2d(vec, name)

    mag = hypot(x, y)
    if mag <= eps:
        return None
    return (x/mag, y/mag)

def angle_2d(vec1: Vector2DLike, vec2: Vector2DLike, *, signed: bool=False, eps: float | None=None) -> float:
    x1, y1 = gd.coerce_vec2d(vec1, "vec1")
    x2, y2 = gd.coerce_vec2d(vec2, "vec2")

    m1 = hypot(x1, y1)
    m2 = hypot(x2, y2)

    threshold = v2.EPSILON if eps is None else eps
    if m1 <= threshold or m2 <= threshold:
        raise ValueError(f"Vector magnitude is too small to compute angle (<= {threshold})!")

    dot_prod = dot_2d(vec1, vec2)
    cross_prod = cross_2d(vec1, vec2)

    if signed:
        angle_rad = atan2(cross_prod, dot_prod)
    else:
        angle_rad = atan2(abs(cross_prod), dot_prod)
    return degrees(angle_rad)
