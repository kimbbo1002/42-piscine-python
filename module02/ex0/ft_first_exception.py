# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 13:26:53 by bokim             #+#    #+#              #
#    Updated: 2026/01/12 13:48:17 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_temperature(temp_str):
	try:
		temp = int(temp_str)
		if 0 <= temp <= 40:
			print(f"Temperature {temp}°C is perfect for plants!")
		elif temp < 0:
			print(f"Temperature {temp}°C is too cold for plants (min 0°C)")
		elif temp > 40:
			print(f"Temperature {temp}°C is too hot for plants (max 40°C)")
	except ValueError:
		print(f"Error: {temp_str} is not a valid number!")

def test_temperature_input():
	print("=== Garden Temperature Checker ===\n")
	print("Testing temperature: 25")
	check_temperature("25")
	print("\nTesting temperature: abc")
	check_temperature("abc")
	print("\nTesting temperature: 100")
	check_temperature("100")
	print("\nTesting temperature: -50")
	check_temperature("-50")
	print("\nAll tests completed - program didn't crash!")

test_temperature_input()