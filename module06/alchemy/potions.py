from alchemy.elements import (
    create_fire as fire, 
    create_water as water, 
    create_earth as earth, 
    create_air as air
)

def healiing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"{fire()} and {water()}"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"{earth()} and {fire()}"
    )


def invisibility_potion() -> str:
    return (
        "Invisibility potion brewed with "
        f"{air()} and {water()}"
    )


def wisdon_potion() -> str:
    return (
        "Wisdom potion brewed with all elements: "
        f"{fire()}, {water()}, {earth()}, and {air()}"
    )