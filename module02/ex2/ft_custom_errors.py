class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Caught a garden error: {message}")


class PlantError(GardenError):
    def __init__(self, name):
        self.name = name
        self.detail = f"The {self.name} plant is wilting!"
        super().__init__(self.detail)

    def error_message(self):
        return f"Plant Error: {self.detail}"


class WaterError(GardenError):
    def __init__(self):
        self.detail = "Not enough water in the tank!"
        super().__init__(self.detail)

    def error_message(self):
        return f"Water Error: {self.detail}"


def check_garden(name, last_water, water_left):
    if last_water >= 5:
        raise PlantError(name)
    if water_left <= 0:
        raise WaterError()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_garden("tomato", 7, 2)
    except PlantError as e:
        print(e.error_message())
    print("\nTesting WaterError...")
    try:
        check_garden("cactus", 3, 0)
    except WaterError as e:
        print(e.error_message())
    print("\nTesting catching all garden errors...")
    try:
        check_garden("tomato", 7, 2)
    except GardenError as e:
        print(e)
    try:
        check_garden("cactus", 3, 0)
    except GardenError as e:
        print(e)
    print("\nAll custom error types work correctly!")
