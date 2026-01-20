def water_plants(plant_list: list):
    print("Opening watering system")
    for plant in plant_list:
        try:
            valid_plant(plant)
            print(f"Watering {plant.name}")
        except WaterError:
            print(f"{WaterError}")
        finally:
            print()

            