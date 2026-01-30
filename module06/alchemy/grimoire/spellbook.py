def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    valid = ["fire", "water", "earth", "air"]
    if any(element in ingredients for element in valid):
        return (
            f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
        )
    else:
        return (
            f"Spell rejected: {spell_name} ({validate_ingredients(ingredients)})"
        )