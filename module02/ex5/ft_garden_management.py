class Plant():
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    plants = []

    def add_plant(name, water, sun):
        try:
            if name == "":
                raise ValueError(
                    "Error adding plant: Plant name cannot be empty!"
                )
            GardenManager.plants.append(Plant(name, water, sun))
            print(f"Added {name} successfully")
        except ValueError as e:
            print(e)

    def water_plants():
        print("Opening watering system")
        for plant in GardenManager.plants:
            print(f"Watering {plant.name} - success")
            plant.water += 1
        print("Closing watering system (cleanup)")

    def check_health():
        try:
            for plant in GardenManager.plants:
                if plant.water < 1:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        "Water level {plant.water} is too low (min 1)"
                    )
                elif plant.water > 10:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        "Water level {plant.water} is too high (max 10)"
                    )
                elif plant.sun < 2:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        "Sunlight hours {plant.sun} is too low (min 2)"
                    )
                elif plant.sun > 12:
                    raise ValueError(
                        f"Error checking {plant.name}: "
                        "Sunlight hours {plant.sun} is too high (max 2)"
                    )
                print(
                    f"{plant.name}: "
                    "healthy (water: {plant.water}, sun: {plant.sun})"
                )
        except ValueError as e:
            print(e)


class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Caught GardenError: {message}")


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
    return "No Garden Errors!"


def test_garden_management():
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    GardenManager.add_plant("tomato", 4, 8)
    GardenManager.add_plant("lettuce", 14, 8)
    GardenManager.add_plant("", 4, 8)
    print("\nWatering plants...")
    GardenManager.water_plants()
    print("\nChecking plant health...")
    GardenManager.check_health()
    print("\nTesting error recovery...")
    water_tank = 0
    try:
        check_garden("rose", 3, water_tank)
    except GardenError as e:
        print(e)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
