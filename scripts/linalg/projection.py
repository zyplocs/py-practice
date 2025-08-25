import guards as gd
from guards import Vector2D, Vector2DLike
from math import hypot

def dot(vec1: Vector2DLike, vec2: Vector2DLike) -> float:
    v1 = gd._coerce_vec(vec1, "vec1")
    v2 = gd._coerce_vec(vec2, "vec2")

    return sum(v1i*v2i for v1i, v2i in zip(v1, v2))

def l2_norm(vec: Vector2DLike, *, name: str="vec") -> float:
    x, y = gd._coerce_vec(vec, name)
    
    return hypot(x, y)

def unit_vector(vec: Vector2DLike, *, eps: float=1e-12, name: str="vec") -> Vector2D | None:
    x, y = gd._coerce_vec(vec, name)

    mag = hypot(x, y)
    if mag <= eps:
        return None
    return (x/mag, y/mag)