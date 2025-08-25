import guards as gd
from guards import NumericTypeError, Vector2DLike, Vector2D
from math import hypot

EPSILON = 1e-6  # close to zero threshold

def vector_sum(vec1: Vector2DLike, vec2: Vector2DLike) -> Vector2D:
    v1 = gd._coerce_vec(vec1, "vec1")
    v2 = gd._coerce_vec(vec2, "vec2")

    return (v1[0] + v2[0], v1[1] + v2[1])

def vector_mag(vec: Vector2DLike, *, name: str="vec") -> float:
    x, y = gd._coerce_vec(vec, name)

    return hypot(x, y)

def unit_vector(vec: Vector2DLike, *, name: str="vec") -> Vector2D:
    x, y = gd._coerce_vec(vec, name)
    mag = hypot(x, y)
    if mag <= EPSILON:
        raise ValueError(f"{name} magnitude is too small to normalize (<= {EPSILON})!")

    return (x/mag, y/mag)

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
            vec1 = gd.parse_vec(vec1_raw, "Vector 1")
            vec2 = gd.parse_vec(vec2_raw, "Vector 2")

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
