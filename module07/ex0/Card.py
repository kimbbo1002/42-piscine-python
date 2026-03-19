from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not name:
            raise ValueError("Card name must be a non-empty string.")
        if cost < 0:
            raise ValueError("Card cost must be a non-negative integer.")
        if not rarity.capitalize() in ["Common", "Rare", "Epic", "Legendary"]:
            raise ValueError("Rarity type does not exist.")
        self.name = name
        self.cost = cost
        self.rarity = rarity.capitalize()

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
