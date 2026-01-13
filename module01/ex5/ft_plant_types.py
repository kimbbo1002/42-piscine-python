# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 14:28:29 by bokim             #+#    #+#              #
#    Updated: 2026/01/13 15:23:59 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name.capitalize()
		self.height = height
		self.age = age

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color
	
	def bloom(self):
		print(f"{self.name} is blooming beautifully!\n")

class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter
	
	def produce_shade(self, x):
		print(f"{self.name} provides {x} square meters of shade\n")

class Vegetable(Plant):
	def __init__(self, name, height, age, harvest, nutritional_value):
		super().__init__(name, height, age)
		self.harveset = harvest
		self.nutritional_value = nutritional_value

if __name__ == "__main__":
	rose = Flower("rose", 25, 30, "red")
	oak = Tree("oak", 500, 1825, 50)
	tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
	print("=== Garden Plant Types ===\n")
	print(f"{rose.name} ({rose.__class__.__name__}): {rose.height}cm, {rose.age} days, {rose.color} color")
	rose.bloom()
	print(f"{oak.name} ({oak.__class__.__name__}): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
	oak.produce_shade(78)
	print(f"{tomato.name} ({tomato.__class__.__name__}): {tomato.height}cm, {tomato.age} days, {tomato.harveset} harvest")
	print(f"{tomato.name} is rich in {tomato.nutritional_value}")