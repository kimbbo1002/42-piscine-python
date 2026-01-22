def valid_plant(plant_name):
    return plant_name in ["tomato", "lettuce", "carrots"]


def ft_len(list):
    count = 0
    for thing in list:
        count += 1
    return count


def water_plants(plant_list: list):
    print("Opening watering system")
    list_len = ft_len(plant_list)
    i = 0
    try:
        for plant in plant_list:
            if not valid_plant(plant):
                raise ValueError(
                    f"Error: Cannot water {plant} - invalid plant"
                )
            print(f"Watering {plant}")
            i += 1
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
        if list_len == i:
            print("Watering completed successfully!")


def test_watering_system():
    good = ["tomato", "lettuce", "carrots"]
    bad = ["tomato", "None"]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(good)
    print("\nTesting with error...")
    water_plants(bad)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
