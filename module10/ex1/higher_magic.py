def spell_combiner(spell1: callable, spell2: callable) -> callable:
    target = "Dragon"
    return lambda: (spell1(target), spell2(target))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    power = 10
    return lambda: multiplier * base_spell(power)


def conditional_caster(condition: callable, spell: callable) -> callable:
    health = 5
    return lambda: spell(condition(health))


def spell_sequence(spells: list[callable]) -> callable:
    return lambda: [spell() for spell in spells]


def main() -> None:
    print("\nTesting spell combiner...")
    res_func1 = spell_combiner(lambda c: f"Fireball hits {c}",
                               lambda c: f"Heals {c}")
    print(f"Combined spell result: {res_func1()}")

    print("\nTesting power amplifier...")
    res_func2 = power_amplifier(lambda power: power, 3)
    print(f"Original: 10, Amplified: {res_func2()}")

    print("\nTesting conditional_caster...")
    res_func3 = conditional_caster(lambda h: h > 0,
                                   lambda b: "Spell casted"
                                   if b else "Spell fizzled")
    print(f"Casted spell result: {res_func3()}")

    print("\nTesting spell_sequence...")
    res_func4 = spell_sequence([lambda: "spell1", lambda: "spell2"])
    print(f"Casted spells: {res_func4()}")


if __name__ == "__main__":
    main()
