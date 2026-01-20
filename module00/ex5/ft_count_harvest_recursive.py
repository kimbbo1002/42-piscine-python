def ft_harvest_recursive(i):
    if i == 0:
        return 0
    ft_harvest_recursive(i - 1)
    print(f"Day {i}")


def ft_count_harvest_recursive():
    print("Days until harvest: 5")
    ft_harvest_recursive(5)
    print("Harvest time!")

# ft_count_harveest_recursive()
