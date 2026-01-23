import sys

def ft_inventory_system() -> None:
    invent = {}
    for item in sys.args[1:]:
        tmp = item.split(':')
        invent[tmp[0]] = tmp[1]
    
    total_items = 