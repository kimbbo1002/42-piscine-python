class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
    
    def base_str(self) -> str:
        return f"Caught a garden error: {self.message}"

    def __str__(self) -> str:
        return f"Caught a garden error: {self.message}"


class PlantError(GardenError):
    def __init__(self, name: str) -> None:
        self.name = name
        self.detail = f"The {self.name} plant is wilting!"
        super().__init__(self.detail)

    def __str__(self) -> str:
        return f"Plant Error: {self.detail}"


class WaterError(GardenError):
    def __init__(self) -> None:
        self.detail = "Not enough water in the tank!"
        super().__init__(self.detail)

    def __str__(self) -> str:
        return f"Water Error: {self.detail}"


def check_garden(name: str, last_water: int, water_left: int) -> None:
    if last_water >= 5:
        raise PlantError(name)
    if water_left <= 0:
        raise WaterError()


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_garden("tomato", 7, 2)
    except PlantError as e:
        print(e)
    print("\nTesting WaterError...")
    try:
        check_garden("cactus", 3, 0)
    except WaterError as e:
        print(e)
    print("\nTesting catching all garden errors...")
    try:
        check_garden("tomato", 7, 2)
    except GardenError as e:
        print(e.base_str())
    try:
        check_garden("cactus", 3, 0)
    except GardenError as e:
        print(e.base_str())
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()