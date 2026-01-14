# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 15:24:31 by bokim             #+#    #+#              #
#    Updated: 2026/01/14 02:25:06 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenManager:
    total_garden = 0

    class GardenStats:
        @staticmethod
        def validate_height(height):
            return height > 0
    
    def __init__(self, name):
        self.name = name
    @classmethod
    def create_garden_network(cls, name):
        print("=== Garden Management System Demo ===")
        return cls(name)
    @staticmethod
    pass:

class Garden(GardenManager):
    def __init__(self, name):
        super().__init__(name)

class Plant():
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.kind = "normal"

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.kind = "flowering"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
        self.kind = "prize"



