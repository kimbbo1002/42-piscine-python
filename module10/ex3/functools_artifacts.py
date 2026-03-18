from functools import reduce, partial, lru_cache, singledispatch
import operator
def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        raise ValueError("Spell list cannot be empty")
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unsupoorted operation.")
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire")
    ice_enchant = partial(base_enchantment, power=50, element="ice")
    light_enchant = partial(base_enchantment, power=50, element="lightning")
    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": light_enchant
    }


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> callable:
    pass


def main() -> None:
    print("\nTesting spell_reducer...")
    data = [1, 2, 3, 4, 5]
    print(f"+ : {spell_reducer(data, "add")}")
    print(f"* : {spell_reducer(data, "multiply")}")
    print(f"max : {spell_reducer(data, "max")}")
    print(f"min : {spell_reducer(data, "min")}")

    print("\nTesting partial enchanter...")
    base = lambda power, element, t: f"{element} enchant, power={power}, target={t}"
    funcs = partial_enchanter(base)
    print(funcs['fire_enchant'](t="target"))
    print(funcs['ice_enchant'](t="target"))
    print(funcs['lightning_enchant'](t="target"))


if __name__ == "__main__":
    main()