import alchemy
from alchemy import (
    lead_to_gold, stone_to_gem, philosophers_stone, elixir_of_life
    )

def main() -> None:
    print("\n=== Pathway Debate Mastery ===\n")
    print(
        "Testing Absolute Imports (from basic.py)\n"
        f"lead_to_gold(): {lead_to_gold()}\n"
        f"stone_to_gem(): {stone_to_gem()}\n"
    )
    print(
        "Testing Relative Imports (from advanced.py)\n"
        f"philosophers_stone(): {philosophers_stone()}\n"
        f"elixir_of_life(): {elixir_of_life()}\n"
    )
    print(
        "Testing Package Access:\n"
        f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}\n"
        f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}\n"
    )
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()