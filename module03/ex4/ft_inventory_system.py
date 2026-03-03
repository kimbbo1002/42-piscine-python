import sys

def inventory_master() -> None:
    invent = {}
    total = 0
    for item in sys.args[1:]:
        tmp = item.split(':')
        invent.update(tmp[0]: tmp[1])
        total += int(tmp[1])
    print(
        "=== Inventory System Analysis ===\n"
        f"Total items in inventory: {total}\n"
        f"Unique item types: {len(invent)}"
    )
    invent_list = invent.items()
    max = 
    print("\n=== Current Inventory===\n")
    for item in invent_list:
        name = item[0]
        unit = int(item[1])
        percent = (unit / total) * 100
        print(f"{name}: {unit} ({percent:.1f}%)")
    