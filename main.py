def divisor(left: int, right: int) -> int:
    """The greatest common divisor, by Euclid's method."""
    while right:
        left, right = right, left % right
    return abs(left)


if __name__ == "__main__":
    print(divisor(1071, 462))
