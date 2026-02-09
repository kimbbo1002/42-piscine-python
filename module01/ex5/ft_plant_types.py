class Plant:
    def __init__(self, name, height, age):
        """This function initiates a plant"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        """This function initiates a flower"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """This function blooms a flower"""
        return f"{self.name} is blooming beautifully!\n"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        """This function initiates a tree"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, x):
        """This function displays shade provided"""
        return f"{self.name} provides {x} square meters of shade\n"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest, nutritional_value):
        """This function initiates a vegetable"""
        super().__init__(name, height, age)
        self.harveset = harvest
        self.nutritional_value = nutritional_value


def main() -> None:
    """This main function displays the flow"""
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===\n")
    print(
        f"{rose.name} ({rose.__class__.__name__}): {rose.height}cm, "
        f"{rose.age} days, {rose.color} color\n"
        f"{rose.bloom()}"
    )
    print(
        f"{oak.name} ({oak.__class__.__name__}): {oak.height}cm, "
        f"{oak.age} days, {oak.trunk_diameter}cm diameter\n"
        f"{oak.produce_shade(78)}"
    )
    print(
        f"{tomato.name} ({tomato.__class__.__name__}): {tomato.height}cm, "
        f"{tomato.age} days, {tomato.harveset} harvest\n"
        f"{tomato.name} is rich in {tomato.nutritional_value}"
    )


if __name__ == "__main__":
    main()