class SecurePlant:
    def __init__(self, name: str, height: int = 0, age: int =0) -> None:
        """This function initiates a plant"""
        self.name = name
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}")

    def set_height(self, tmp_height: int) -> None:
        """This function checks height """
        if tmp_height >= 0:
            self.height = tmp_height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print(
                f"\nInvalid operation attempted: height {tmp_height}cm "
                "[REJECTED]"
                "Security: Negative height rejected\n"
            )

    def get_height(self) -> int:
        """This function displays height"""
        return self.height

    def set_age(self, tmp_age: int) -> None:
        """This function sets age"""
        if tmp_age >= 0:
            self.age = tmp_age
            print(f"Age updated: {self.age} days [OK]")
        else:
            print(
                f"Invalid operation attempted: height {tmp_age}cm "
                "[REJECTED]\n"
                "Security: Negative height rejected"
            )

    def get_age(self) -> int:
        """This function displays age"""
        return self.age


def main() -> None:
    """This main function displays the flow"""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(
        f"Current plant: {rose.name} ({rose.get_height()}cm, "
        f"{rose.get_age()} days)"
    )

if __name__ == "__main__":
    main()
