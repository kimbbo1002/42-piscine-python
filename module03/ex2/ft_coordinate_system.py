import math


def get_dist(pos: tuple) -> None:
    dist = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
    print(
        f"Distance between (0, 0, 0) and {pos}: {dist:.2f}\n"
    )


def parse_args(string: str) -> tuple:
    raw = string.split(',')
    pos = []
    i = 0
    try:
        for val in raw:
            pos.append(int(val))
            i += 1
        pos = tuple(pos)
        print(f'Parsing coordinates: "{string}"')
        print(f"Parsed position: {pos}")
        get_dist(pos)
        return pos
    except ValueError:
        print(
            f'Parsing invalid coordinates: "{string}"\n'
            "Error parsing coordinates: "
            f"invalid literal for int() with base 10: '{raw[i]}'\n"
            "Error details - Type: ValueError, Args: "
            f"(invalid literal for int() with base 10: '{raw[i]}')\n"
        )
        return


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    ex1 = (10, 20, 5)
    print(f"Position created: {ex1}")
    get_dist(ex1)
    ex2 = "3,4,0"
    tup = parse_args(ex2)
    try:
        ex3 = "abc,def,ghi"
        parse_args(ex3)
    except TypeError:
        pass
    print("Unpacking demonstration:")
    x, y, z = tup
    print(
        f"Player at x={x}, y={y}, z={z}\n"
        f"Foordinates: X={x}, Y={y}, Z={z}"
    )


ft_coordinate_system()
