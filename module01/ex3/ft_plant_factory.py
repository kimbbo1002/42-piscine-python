class Plant:
    total = 0

    def __init__(self, name, height, age) -> None:
        """This function initiates a plant"""
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1
        print(f"Created: {self.name} ({height}cm, {age} days)")


def main() -> None:
    """This main function displays the flow"""
    plant_to_create = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for data in plant_to_create:
        Plant(*data)
    print(f"\nTotal plants created: {Plant.total}")


if __name__ == "__main__":
    main()
