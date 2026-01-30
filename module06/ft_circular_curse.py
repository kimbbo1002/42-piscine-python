from alchemy import record_spell, validate_ingredients

def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    print(
        "Testing ingredient validation:\n"
        f'validate_ingredients("fire air"): {validate_ingredients("fire air")}\n'
        f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}\n'
    )
    print(
        "Testing spell recording with validation:\n"
        f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}\n'
        f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}\n'
    )
    print(
        "Testing late import technique:\n"
        f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}\n'
    )
    print(
        "Circular dependency curse avoided using late imports!\n"
        "All spells processed safely!"
    )


if __name__ == "__main__":
    main()