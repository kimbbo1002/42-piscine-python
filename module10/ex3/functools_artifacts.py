from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


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
        raise ValueError("Unsupoorted operation.")
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


@lru_cache(maxsize=128, typed=False)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatch(spell: Any) -> None:
        print("\nUnsupported spell type")

    @dispatch.register(int)
    def _(spell: int) -> None:
        print(f"Spell of {spell} power dispatched.")

    @dispatch.register
    def _(spell: str) -> None:
        print(f"{spell} spell dispatched.")

    @dispatch.register
    def _(spells: list) -> None:
        print("Casted spells:")
        for spell in spells:
            print(f"- {spell}")
    return dispatch


def main() -> None:
    print("\nTesting spell_reducer...")
    data = [1, 2, 3, 4, 5]
    print(f"+ : {spell_reducer(data, 'add')}")
    print(f"* : {spell_reducer(data, 'multiply')}")
    print(f"max : {spell_reducer(data, 'max')}")
    print(f"min : {spell_reducer(data, 'min')}")

    print("\nTesting partial enchanter...")
    funcs = partial_enchanter(lambda power, element, t:
                              f"{element} enchant, "
                              f"power={power}, target={t}")
    print(funcs['fire_enchant'](t="target"))
    print(funcs['ice_enchant'](t="target"))
    print(funcs['lightning_enchant'](t="target"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    f = spell_dispatcher()
    f("Smoke")
    f(2)
    f(["test1", "test2"])


if __name__ == "__main__":
    main()
