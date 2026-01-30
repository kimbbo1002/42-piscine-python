from .basic import lead_to_gold
from ..potions import healiing_potion

def philosophers_stone() -> str:
    return (
        "Philosopherś stone created using "
        f"{lead_to_gold()} and {(healiing_potion())}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"