from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if effect_type not in ["damage", "heal"]:
            raise TypeError("Effect type does not exist.")
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"
        self.used = False

    def play(self, game_state: dict) -> dict:
        if game_state["playing"] is False:
            raise ValueError("[ERROR] Game has not started yet!")
        effect_map = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost * 2} health"
        }
        self.used = True
        effect_display = effect_map.get(self.effect_type)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_display
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = self.type
        info["effect_type"] = self.effect_type
        return info
