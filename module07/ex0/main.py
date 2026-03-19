from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("\n=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:")

        game_state = {"playing": True}
        fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        print("\nCreatureCard Info:")
        print(fire_dragon.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        print(f"Playable: {fire_dragon.is_playable(6)}")
        print(f"Play result: {fire_dragon.play(game_state)}")

        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {fire_dragon.attack_target('Goblin Warrior')}")

        print("\nTesting insufficient mana (3 available):")
        print(f"Playable: {fire_dragon.is_playable(3)}")

        print("\nTesting play when game has not started (error)")
        game_state["playing"] = False
        fire_dragon.play(game_state)
    except Exception as e:
        print(e)
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
