from typing import Optional
from ex0 import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class Player:
    def __init__(self, name: str, mana: int = 10, health: int = 30) -> None:
        self.name = name
        self.health = health
        self.mana = mana
        self.hand = []

    def draw(self, card: Card) -> None:
        self.hand.append(card)

    def play_card(self, card: Card) -> bool:
        if card not in self.hand or self.mana < card.cost:
            return False
        self.mana -= card.cost
        self.hand.remove(card)
        return True

    def get_player_info(self) -> str:
        return f"Player({self.name}, hp={self.health}, mana={self.mana})"


class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.player: Optional[Player] = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.player = Player("bokim")
        strategy.player = self.player
        self.strategy = strategy

        for card in [factory.create_creature("dragon"),
                     factory.create_creature("goblin"),
                     factory.create_spell("lightning")]:
            self.player.draw(card)
            self.cards_created += 1

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine not configured.")
        hand = [f"{c.name} ({c.cost})" for c in self.player.hand]
        result = self.strategy.execute_turn(self.player.hand, ['Enemy Player'])
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        return {
            "hand": hand,
            "turn_result": result,
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (
                self.strategy.get_strategy_name() if self.strategy else None
            ),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
            "player_info": self.player.get_player_info()
        }
