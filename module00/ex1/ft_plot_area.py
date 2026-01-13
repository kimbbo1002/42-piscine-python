# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 11:38:16 by bokim             #+#    #+#              #
#    Updated: 2026/01/12 13:20:11 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	area = length * width
	print(f"Plot area: {area}")

# ft_plot_area()