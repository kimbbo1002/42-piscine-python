def ft_harvest_recursive(i: int) -> None:
    if i == 0:
        return 0
    ft_harvest_recursive(i - 1)
    print(f"Day {i}")


def ft_count_harvest_recursive() -> None:
	day = int(input("Days until harvest: "))
	ft_harvest_recursive(day)
	print("Harvest time!")

# ft_count_harvest_recursive()
