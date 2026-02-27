from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from enum import Enum


class effects(Enum):
    DAMAGE = "damage"
    HEAL = "heal"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, effects):
            raise ValueError(
                f"effect_type must be an EffectType enum value."
            )
        self.effect_type = effect_type
        self.type = "Spell"
        self.used = False
    
    def play(self, game_state: dict) -> dict:
        if game_state["playing"] == False:
            raise ValueError("[ERROR] Game has not started yet!")
        self.used = True
        if self.effect_type == "heal":
            effect = "Deal 3 damage to target"
        else:
            effect = "Heal 3 health to creatures"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }
    
    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }