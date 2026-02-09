class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """This function initiates a plant"""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(
            f"{self.name}: {self.height}cm, {self.age} days old"
        )


def main() -> None:
    """This main function displays the flow"""
    rose = Plant("Rose", 25, 30)
    sun = Plant("Sunflower", 80, 45)
    cact = Plant("Cactus", 15, 120)
    print("=== Garen Plant Registry ===")
    rose.display_info()
    sun.display_info()
    cact.display_info()


if __name__ == "__main__":
    main()
