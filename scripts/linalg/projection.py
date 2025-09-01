from vectors2d import Vector2D

def main():
    vec1 = Vector2D(4, 3)
    vec2 = Vector2D(0, 1)

    print(f"Vector 1: {vec1}")
    print(f"Vector 2: {vec2}")
    print(f"Dot product: {vec1.dot(vec2)}")
    print(f"Cross product: {vec1.cross(vec2)}")
    print(f"Angle between: {vec1.angle_to(vec2):.2f} degrees")


if __name__ == "__main__":
    main()