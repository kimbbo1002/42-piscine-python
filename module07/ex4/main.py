from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    try:
        print("\n=== DataDeck Tournament Platform ===\n")
        platform = TournamentPlatform()

        dragon = TournamentCard("dragon", 5, "Legendary", 7, 5, 1200)
        wizard = TournamentCard("wizard", 4, "Rare", 5, 6, 1150)

        print("Registering Tournament Cards...")
        dragon_id = platform.register_card(dragon)
        wizard_id = platform.register_card(wizard)

        for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
            info = card.get_rank_info()
            print(f"\n{card.name} (ID: {card_id}):")
            print("- Interfaces: [Card, Combatable, Rankable]")
            print(f"- Rating: {info['rating']}")
            print(f"- Record: {info['wins']}-{info['losses']}")

        print("\nCreating tournament match...")
        result = platform.create_match(dragon_id, wizard_id)
        print(f"Match result: {result}")

        print("\nTournament Leaderboard:")
        for rank, entry in enumerate(platform.get_leaderboard(), 1):
            card = platform.cards[entry["card_id"]]
            print(
                f"{rank}. {card.name} "
                f"- Rating: {entry['rating']} "
                f"({entry['wins']}-{entry['losses']})"
            )

        print(f"\nPlatform Report:\n{platform.generate_tournament_report()}")
    except Exception as e:
        print(e)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
