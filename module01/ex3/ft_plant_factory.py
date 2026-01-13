# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 13:23:43 by bokim             #+#    #+#              #
#    Updated: 2026/01/13 14:14:41 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name.capitalize()
		self.height = height
		self.age = age
		print(f"Created: {self.name} ({height}cm, {age} days)")

plant_to_create = [
	("rose", 25, 30),
	("oak", 200, 365),
	("cactus", 5, 90),
	("sunflower", 80, 45),
	("fern", 15, 120)
]
	
if __name__ == "__main__":
	print("=== Plant Factory Output ===")
	count = 0
	for data in plant_to_create:
		Plant(*data)
		count += 1
	print(f"\nTotal plants created: {count}")