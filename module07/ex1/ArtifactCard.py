from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
    ) -> None:
        if durability <= 0:
            raise ValueError("Durability must be a positive integer.")
        super().__init__(name, cost, rarity)
        self.type = "Artifact"
        self.durability = durability
        self.effect = effect
        self.active = False

    def play(self, game_state: dict) -> dict:
        if game_state["playing"] is False:
            raise ValueError("[ERROR] Game has not started yet!")
        self.active = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        if not self.active:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "Not playing"
            }
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "Destroyed"
            }
        self.durability -= 1
        return {
            "artifact": self.name,
            "activated": True,
            "effect": self.effect,
            "durability_remaining": self.durability
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = self.type
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
