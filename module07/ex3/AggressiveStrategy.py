from ex0 import Card, CreatureCard
from ex1 import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        players = [t for t in available_targets if t == "Enemy Player"]
        creatures = [t for t in available_targets if t != "Enemy Player"]
        return players + creatures

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        targets_attacked = []
        damage = 0
        mana_used = 0

        for card in hand:
            if not isinstance(card, Card):
                raise ValueError("Error in hand list")
        for card in battlefield:
            if not isinstance(card, str):
                raise ValueError("Error in battlefield list")

        targets = self.prioritize_targets(battlefield)

        for card in sorted(hand, key=lambda c: c.cost):
            if self.player and targets and self.player.play_card(card):
                if isinstance(card, CreatureCard):
                    target = targets.pop(0)
                    targets_attacked.append(target)
                    damage += card.attack
                elif isinstance(card, SpellCard):
                    if card.effect_type == "damage":
                        target = targets.pop(0)
                        targets_attacked.append(target)
                        damage += card.cost
                    else:
                        self.player.health += card.cost * 2
                else:
                    self.player.health += 1
                cards_played.append(card.name)
                mana_used += card.cost
            else:
                continue

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage,
        }
