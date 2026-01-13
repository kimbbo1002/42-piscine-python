# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 11:42:02 by bokim             #+#    #+#              #
#    Updated: 2026/01/12 13:20:59 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")

# ft_plant_age()