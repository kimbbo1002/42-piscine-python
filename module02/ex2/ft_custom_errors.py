class GardenError(Exception):
    def __init__(self, message):
        super().__init__(f"Caught a garden error: {message}")


class PlantError(GardenError):
    def __init__(self, name, last_water):
        self.name = name
        self.last_water = last_water
        self.message = "Caught PlantError: "
        super().__init__(f"The {self.name} plant is wilting!")

    def error_message(self):
        return f"{self.message}The {self.name} is plant wilting!"


class WaterError(GardenError):
    def __init__(self, name, water_left):
        self.name = name
        self.water_left = water_left
        self.message = "Caught WaterError: "
        super().__init__("Not enough water in the tank!")

    def error_message(self):
        return f"{self.message}Not enough water in the tank!"


def check_garden(name, last_water, water_left, garden: bool):
    if last_water >= 5:
        if garden:
            raise GardenError(
                f"{PlantError(name, last_water).error_message()}"
            )
        raise PlantError(name, last_water)
    if water_left <= 0:
        if garden:
            raise GardenError(
                f"{WaterError(name, water_left).error_message()}"
            )
        raise WaterError(name, water_left)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_garden("tomato", 7, 2, False)
    except PlantError as e:
        print(f"{e.error_message()}\n")
    print("Testing WaterError...")
    try:
        check_garden("cactus", 3, 0, False)
    except WaterError as e:
        print(f"{e.error_message()}\n")
    print("Testing catching all garden errors...")
    try:
        check_garden("tomato", 7, 2, False)
    except (PlantError, WaterError) as e:
        print(f"{e}")
    try:
        check_garden("cactus", 3, 0, False)
    except (PlantError, WaterError) as e:
        print(f"{e}\n")
    print("All custom error types work correctly!")
