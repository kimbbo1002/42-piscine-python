import random
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
from ex3.CardFactory import CardFactory
from typing import Optional, Union


class FantasyCardFactory(CardFactory):
    CREATURES = [
        ("Fire Dragon", 5, "Legendary", 7, 5),
        ("Goblin Warrior", 2, "Common", 2, 1),
        ("Ice Golem", 4, "Rare", 3, 6)
    ]

    SPELLS = [
        ("Fireball", 4, "Rare", "damage"),
        ("Lightning Bolt", 3, "Common", "damage"),
        ("Healing Wave", 2, "Common", "heal"),
    ]

    ARTIFACTS = [
        ("Mana Ring", 1, "Common", 3, "+1 health per turn")
    ]

    SUPPORTED = {
        "creatures": ["dragon", "goblin", "golem"],
        "spells": ["fireball", "lightning", "wave"],
        "artifacts": ["ring"],
    }

    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            for data in self.CREATURES:
                if name_or_power.lower() in data[0].lower():
                    return CreatureCard(*data)
        random_card = CreatureCard(*random.choice(self.CREATURES))
        if isinstance(name_or_power, int):
            random_card.attack = name_or_power
        return random_card

    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            for data in self.SPELLS:
                if name_or_power.lower() in data[0].lower():
                    return SpellCard(*data)
        return SpellCard(*random.choice(self.SPELLS))

    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            for data in self.ARTIFACTS:
                if name_or_power.lower() in data[0].lower():
                    return ArtifactCard(*data)
        random_card = ArtifactCard(*random.choice(self.ARTIFACTS))
        if isinstance(name_or_power, int):
            random_card.durability = name_or_power
        return random_card

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for _ in range(size // 3):
            cards.append(self.create_creature())
        for _ in range(size // 3):
            cards.append(self.create_spell())
        for _ in range(size - 2 * (size // 3)):
            cards.append(self.create_artifact())
        return {"theme": "Fantasy", "size": len(cards), "cards": cards}

    def get_supported_types(self) -> dict:
        return self.SUPPORTED
