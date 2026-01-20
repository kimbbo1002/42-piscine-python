class SecurePlant:
    def __init__(self, name, height=0, age=0):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}")

    def set_height(self, tmp_height):
        if tmp_height >= 0:
            self.height = tmp_height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print(
                f"\nInvalid operation attempted: height {tmp_height}cm "
                "[REJECTED]"
                "Security: Negative height rejected\n"
            )

    def get_height(self):
        return self.height

    def set_age(self, tmp_age):
        if tmp_age >= 0:
            self.age = tmp_age
            print(f"Age updated: {self.age} days [OK]")
        else:
            print(
                f"Invalid operation attempted: height {tmp_age}cm "
                "[REJECTED]"
                "Security: Negative height rejected"
            )

    def get_age(self):
        return self.age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(
        f"Current plant: {rose.name} ({rose.get_height()}cm, "
        f"{rose.get_age()} days)"
    )
