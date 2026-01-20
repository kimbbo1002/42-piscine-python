class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sun = Plant("Sunflower", 80, 45)
cact = Plant("Cactus", 15, 120)
if __name__ == "__main__":
    print(
        f"{rose.name}: {rose.height}cm, {rose.age} days old"
        f"{sun.name}: {sun.height}cm, {sun.age} days old"
        f"{cact.name}: {cact.height}cm, {cact.age} days old"
    )
