from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    try:
        print("\n=== DataDeck Game Engine ===\n")

        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        engine = GameEngine()

        print("Configuring Fantasy Card Game...")
        print("Factory: FantasyCardFactory")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

        engine.configure_engine(factory, strategy)

        print("\nSimulating aggressive turn...")
        turn = engine.simulate_turn()

        print(f"Hand: {turn['hand']}")

        result = turn["turn_result"]
        print("\nTurn execution:")
        print(f"Strategy: {result['strategy']}")
        actions = {
            "cards_played": result["cards_played"],
            "mana_used": result["mana_used"],
            "targets_attacked": result["targets_attacked"],
            "damage_dealt": result["damage_dealt"],
        }
        print(f"Actions: {actions}")

        print(f"\nGame Report:\n{engine.get_engine_status()}")
    except Exception as e:
        print(e)
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
