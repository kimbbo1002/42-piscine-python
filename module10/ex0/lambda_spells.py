def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda m: m['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda s: "* " + s + " *", spells)


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    if not mages:
        avg_power = 0
    else:
        avg_power = (
            round(sum(map(lambda m: m['power'], mages))
                  / len(mages), 2)
        )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:

    print("Testing artifact sorter...")
    artifact = [
        {"name": "Fire Staff", "power": 92, "type": "artifact"},
        {"name": "Crystal Orb", "power": 85, "type": "artifact"}
    ]
    for a in artifact_sorter(artifact):
        print(f"- {a['name']} ({a['power']})")

    print("\nTesting power filter...")
    mages = [
        {"name": "Fire Staff", "power": 92, "element": "fire"},
        {"name": "Crystal Orb", "power": 85, "element": "crystal"}
    ]
    for m in power_filter(mages, 90):
        print(f"- {m['name']} ({m['power']})")

    print("\nTesting spell transformer")
    spells = ["fireball", "heal", "shield"]
    for s in spell_transformer(spells):
        print(s)

    print("\nTesting mage stats")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
