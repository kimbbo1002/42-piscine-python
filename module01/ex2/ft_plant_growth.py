class Plant:
    def __init__(self, name: str, height: int, age_day: int) -> None:
        """This function initiates a plant"""
        self.name = name
        self.height = height
        self.age_day = age_day

    def grow(self) -> None:
        """This function grows the plant"""
        self.height += 1

    def age(self) -> None:
        """This function ages the plant"""
        self.age_day += 1

    def get_info(self) -> None:
        """This function gets info of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")


def main() -> None:
    """This main function displays the flow"""
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    h1 = rose.height
    for i in range(1, 7):
        rose.age()
        rose.grow()
    print("=== Day 7 ===")
    rose.get_info()
    h2 = rose.height
    print(f"Growth this week: +{h2 - h1}cm")


if __name__ == "__main__":
    main()
