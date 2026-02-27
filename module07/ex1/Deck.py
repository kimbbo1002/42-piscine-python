from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Cards can be added")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.remove(i)
                return True
        return False
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def draw_card(self) -> Card:
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
            if card.type == "Creature":
                creature += 1
            elif card.type == "Spell":
                spell += 1
            else:
                artifact += 1
            cost += card.cost
        return {
            "total_cards": total,
            "creatures": creature,
            "spells": spell,
            "artifacts": artifact,
            "avg_cost": round(cost / total if total else 0.0, 1)
        }