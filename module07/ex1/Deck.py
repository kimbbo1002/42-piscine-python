import random
from typing import List, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added.")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creature = 0
        spell = 0
        artifact = 0
        cost = 0.0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                creature += 1
            elif card.type == "Spell":
                spell += 1
            else:
                artifact += 1
            cost += card.cost
        avg_cost = round(cost / total, 1) if total > 0 else 0.0
        return {
            "total_cards": total,
            "creatures": creature,
            "spells": spell,
            "artifacts": artifact,
            "avg_cost": avg_cost
        }
