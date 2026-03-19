from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        print("Building deck with different card types...")

        # creating cards
        fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        lighting = SpellCard("Lightning Bolt", 3, "Rare", "damage")
        crystal = ArtifactCard("Mana Crystal", 2,
                               "Common", 5, "+1 mana per turn")

        # creating deck
        deck = Deck()
        deck.add_card(fire_dragon)
        deck.add_card(lighting)
        deck.add_card(crystal)
        deck.shuffle()

        game_state = {"playing": True}

        print(f"Deck stats: {deck.get_deck_stats()}")

        print("\nDrawing and playing cards:")

        c1 = deck.draw_card()
        c2 = deck.draw_card()
        c3 = deck.draw_card()

        for card in [c1, c2, c3]:
            print(
                f"\nDrew: {card.name} ({card.type})\n"
                f"Play result: {card.play(game_state)}"
            )
    except Exception as e:
        print(e)
    print(
            "\nPolymorphism in action: Same interface, "
            "different card behaviors!"
        )


if __name__ == "__main__":
    main()
