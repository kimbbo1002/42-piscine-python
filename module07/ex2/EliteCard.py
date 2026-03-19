from ex0 import Card, CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from enum import Enum
from typing import Any


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        mana: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana
        self.health = health
        self.type = CardType.ELITE

    # Card
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = self.type
        info["attack"] = self.attack_power
        info["defense"] = self.defense
        info["mana"] = self.mana
        return info

    def play(self, game_state: dict) -> dict:
        if game_state["playing"] is False:
            raise ValueError("[ERROR] Game has not started yet!")
        return {
            "card_played": self.name,
            "mana_used": self.cost
        }

    # Combatable
    def attack(self, target: Any) -> dict:
        if not isinstance(target, (str, CreatureCard)):
            raise TypeError("Enter target name or target card.")
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
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

    # Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self.mana < self.cost:
            raise ValueError("Cannot cast spell (not enough mana)")
        cost = self.cost
        self.mana = max(0, self.mana - cost)
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana": self.mana
        }
