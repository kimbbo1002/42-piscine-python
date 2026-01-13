# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_error.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bokim <bokim@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 13:48:42 by bokim             #+#    #+#              #
#    Updated: 2026/01/12 14:00:09 by bokim            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations():
	try:
		tmp = int("abc")
	except ValueError:
		print("Caught Value Error: invalid literal for int()")
	try:
		tmp = 1/0
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero")
	try: 
	
def test_error_types():
	print("=== Garden Error Types Demo ===\n")
	print("\n Testing Value error...")
	garden_operations()

	print("\nAll error types tested successfully!")