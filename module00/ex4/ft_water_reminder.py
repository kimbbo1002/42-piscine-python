# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 11:43:27 by bokim             #+#    #+#              #
#    Updated: 2026/01/12 13:21:11 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	day = int(input("Days since last watering: "))
	if day > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")

# ft_water_reminder()