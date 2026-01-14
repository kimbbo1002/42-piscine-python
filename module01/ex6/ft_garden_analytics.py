class Plant():
	def __init__(self, name, height):
		self.name = name
		self.height = height
		self.kind = "regular"
	def grow(self):
		self.height += 1
	def get_info(self):
		return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
	def __init__(self, name, height, color):
		super().__init__(name, height)
		self.color = color
		self.kind = "flowering"
	def get_info(self):
		base_info = super().get_info()
		return f"{base_info}, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, color, points):
		super().__init__(name, height, color)
		self.points = points
		self.kind = "prize"
	def get_info(self):
		base_info = super().get_info()
		return f"{base_info}, Prize points: {self.points}"

class GardenManager():
	total_gardens = 0
	gardens = []
	def __init__(self, name):
		self.name = name
		self.plants = []
		self.total_growth = 0
		self.score = 0
		GardenManager.total_gardens += 1
		GardenManager.gardens.append(self)

	class GardenStats():
		@staticmethod
		def manage_report(plants: list, total_growth):
			total = 0
			regular = 0
			flower = 0
			prize = 0
			for plant in plants:
				total += 1
				if plant.kind == "regular":
					regular += 1
				if plant.kind == "flowering":
					flower += 1
				else:
					prize += 1
			print(f"\nPlants added: {total}, Total growth: {total_growth}cm")
			print(f"Plant types: {regular} regular, {flower} flowering, {prize} prize flowers")
		
		@staticmethod
		def count_score(plants: list):
			score = 0
			for plant in plants:
				if plant.kind == "prize":
					score += plant.points
			return score
	
	@classmethod
	def create_garden_network(cls):
		print("Garden scores:")
		for garden in cls.gardens:
			score = garden.GardenStats.count_score(garden.plants)
			print(f"- {garden.name}: {score}")
		print(f"Total gardens managed: {cls.total_gardens}")
	
	def add_plant(self, plant: Plant):
		self.plants.append(plant)
		print(f"Added {plant.name} to {self.name}'s garden")
	
	def manage_growth(self):
		print(f"\n{self.name} is helping all plants grow ...")
		for plant in self.plants:
			plant.grow()
			self.total_growth += 1
	
	@staticmethod
	def validate_height(plants: list):
		tmp = True
		for plant in plants:
			if plant.height < 0:
				tmp = False
		return tmp

	
	def display_report(self):
		print(f"\n=== {self.name}'s Garden Report ===")
		print("Plants in garden:")
		for plant in self.plants:
			info = plant.get_info()
			print(f"- {plant.name}: {info}")
		GardenManager.GardenStats.manage_report(self.plants, self.total_growth)
		print(f"\nHeight Validation test: {GardenManager.validate_height(self.plants)}")
		GardenManager.create_garden_network()


if __name__ == "__main__":
	print("=== Garden Management System Demo ===\n")

	alice = GardenManager("Alice")
	oak = Plant("Oak Tree", 101)
	rose =  FloweringPlant("Rose", 26, "red")
	sun = PrizeFlower("Sunflower", 51, "yellow", 10)

	alice.add_plant(oak)
	alice.add_plant(rose)
	alice.add_plant(sun)

	alice.manage_growth()

	bob = GardenManager("Bob")
	cactus = PrizeFlower("Cactus", 91, "green", 92)
	bob.add_plant(cactus)

	alice.display_report()
