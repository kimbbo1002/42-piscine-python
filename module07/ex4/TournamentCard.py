from ex0 import Card
from ex2 import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack_power: int,
            defense: int,
            rating: int
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.health = defense
        self.wins = 0
        self.losses = 0
        self.rating = rating

    # Card
    def play(self, game_state: dict) -> dict:
        if game_state["playing"] is False:
            raise ValueError("[ERROR] Game has not started yet!")
        return {
            "card_played": self.name,
            "mana_used": self.cost
        }

    # Combatable
    def attack(self, target) -> dict:
        if not isinstance(target, (Card, str)):
            raise ValueError(
                "Target needs to be a Card instance or name of target"
            )
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        taken = max(0, incoming_damage - blocked)
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack_power,
            "defense": self.defense,
            "current_health": self.health
        }

    # Rankable
    def calculate_rating(self) -> int:
        return self.rating + (self.wins - self.losses) * 16

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {**self.get_card_info(), **self.get_rank_info()}
