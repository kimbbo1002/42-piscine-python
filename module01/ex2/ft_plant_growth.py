# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 13:07:03 by bokim             #+#    #+#              #
#    Updated: 2026/01/13 14:14:58 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age_day: int):
        self.name = name.capitalize()
        self.height = height
        self.age_day = age_day
    def grow(self):
           self.height += 1
    def age(self):
           self.age_day += 1
    def get_info(self):
            print(f"{self.name}: {self.height}cm, {self.age_day} days old")

if __name__ == "__main__":
      rose = Plant("rose", 25, 30)
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
            
            