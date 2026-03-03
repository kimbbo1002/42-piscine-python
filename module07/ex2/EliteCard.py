from Combatable import Combatable
from Magical import Magical
from ex0 import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int, combat_type: str, defense: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.combat_type = combat_type
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        if game_state["state"] == "playing":
            return {
                "name": self.name,
                "type": "Elite"
            }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - self.defense,
            "damage_blocked": self.defense,
            "still_alive": self.health - (incoming_damage - self.defense) > 0
        }

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets:list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        pass
