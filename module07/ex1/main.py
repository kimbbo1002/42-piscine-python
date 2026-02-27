from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, effects
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    
    # creating cards
    fire_dragon = CreatureCard("Fire Dragon", 5, "lengendary", 7, 5)
    lighting = SpellCard("Lightning Bolt", 3, "common", effects.DAMAGE)
    crystal = ArtifactCard("Mana Crystal", 2, "common", 5, "+1 mana per turn")

    # creating deck
    deck = Deck()
    deck.add_card(fire_dragon)
    deck.add_card(lighting)
    deck.add_card(crystal)
    deck.shuffle()

    game_state = {
        "player": "bokim",
        "playing": True
    }

    print("Building deck with different card types...")
    print(
        "Deck stats: "
        f"{deck.get_deck_stats()}"
    )

    print("\n Drawing and playing cards:")

    c1 = deck.draw_card()
    c2 = deck.draw_card()
    c3 = deck.draw_card()

    print(
        f"\nDrew: {c1.name} ({c1.type})\n"
        f"Play result: {c1.play(game_state)}"
    )

    print(
        f"\nDrew: {c2.name} ({c2.type})\n"
        f"Play result: {c2.play(game_state)}"
    )

    print(
        f"\nDrew: {c3.name} ({c3.type})\n"
        f"Play result: {c3.play(game_state)}"
    )

    print("\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()