def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be emtpy!")
        elif water_level < 1:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
            )
        elif water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
            )
        elif sunlight_hours < 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 2)"
            )
        print(f"Plant {plant_name} is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 3, 6)
    print("\nTesting empty plant name")
    check_plant_health("", 3, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 3)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
