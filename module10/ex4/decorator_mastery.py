from datetime import datetime
from functools import wraps
from typing import Any


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper() -> Any:
        print(f"Casting {func.__name__}...")
        start = datetime.now()
        res = func()
        end = datetime.now()
        time = end - start
        print(f"Spell completed in {time} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(power: int) -> Any:
            if power >= min_power:
                return func(power)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    if max_attempts <= 0:
        raise ValueError("max attempts should be a positive integer")

    def decorator(func: callable) -> callable:
        attempt = 0

        @wraps(func)
        def wrapper() -> Any:
            nonlocal attempt
            while attempt < max_attempts:
                attempt += 1
                try:
                    return func()
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    def __init__(self, guild_name: str, power: int):
        self.guild_name = guild_name
        self.power = power

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3 or name.replace(" ", "").isalpha():
            return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        if power > self.power:
            return "Insufficient power for this spell"
        self.power -= power
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")
    f = spell_timer(lambda: "this is a test")
    print(f"testing function: {f.__name__}")
    f()

    print("\nTesting power validator...")
    f = power_validator(10)
    deco = f(lambda p: f"Casted Fire spell, {p - 5} power left.")
    print(f"testing function: {deco.__name__}")
    print(deco(15))

    print("\nTesting retry spell")
    try:
        f = retry_spell(5)
        deco = f(lambda: int("a"))
        print(f"testing function: {deco.__name__}")
        print(deco())
    except Exception as e:
        print(e)

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("bokim"))
    print(MageGuild.validate_mage_name("bokim123"))
    bokim = MageGuild("bokim", 20)
    print(bokim.cast_spell("Lightning", 15))
    print(bokim.cast_spell("Lightning", 15))


if __name__ == "__main__":
    main()
