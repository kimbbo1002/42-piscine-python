from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulator() -> int:
        nonlocal total_power
        total_power += initial_power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:

    def enchante(item_name: str) -> str:
        return enchantment_type + item_name
    return enchante


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    f = mage_counter()
    for i in range(3):
        print(f"Call 1: {f()}")

    print("\nTesting spell accumulator...")
    f = spell_accumulator(5)
    for i in range(3):
        print(f"Call 1: {f()}")

    print("\nTesting enchantment factory...")
    f = enchantment_factory("Flaming")
    print(f("Sword"))
    f = enchantment_factory("Frozen")
    print(f("Shield"))

    print("\nTesting memory vault...")
    funcs = memory_vault()
    funcs["store"]("key", 1)
    print(funcs["recall"]("key"))


if __name__ == "__main__":
    main()
