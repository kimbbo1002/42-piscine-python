from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    try:
        arcane_warrior = EliteCard("Arcane Warrior",
                                   4, "Legendary", 5, 3, 8, 5)
        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

        print(
            f"\nPlaying {arcane_warrior.name} "
            f"({arcane_warrior.type.value}):"
        )

        print("\nCombat phase:")
        print(f"Attack result: {arcane_warrior.attack('Enemy')}")
        print(f"Defense result: {arcane_warrior.defend(5)}")

        print("\nMagic phase:")
        print(
            "Spell cast: "
            f"{arcane_warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
        )
        print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    except Exception as e:
        print(e)
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
