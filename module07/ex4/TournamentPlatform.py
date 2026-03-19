from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches: List[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.lower().replace(" ", "_") + "_001"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("register the cards first!")
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]

        if c1.attack_power >= c2.attack_power:
            winner_id, loser_id = card1_id, card2_id
        else:
            winner_id, loser_id = card2_id, card1_id

        self.cards[winner_id].update_wins(1)
        self.cards[loser_id].update_losses(1)

        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": self.cards[winner_id].calculate_rating(),
            "loser_rating": self.cards[loser_id].calculate_rating(),
        }
        self.matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        standings = [
            {"card_id": cid, **card.get_rank_info()}
            for cid, card in self.cards.items()
        ]
        return sorted(standings, key=lambda x: x["rating"], reverse=True)

    def generate_tournament_report(self) -> dict:
        ratings = [c.calculate_rating() for c in self.cards.values()]
        avg = sum(ratings) // len(ratings) if ratings else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self.matches),
            "avg_rating": avg,
            "platform_status": "active",
        }
