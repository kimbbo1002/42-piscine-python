def ft_achievement_tracker() -> None:
    ach = {"boss_slayer", "collector", "first_kill",
           "level_10", "perfectionist", "speed_demmon", "treasure_hunter"}
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter",
               "boss_slayer", "speed_demon", "perfectionist"}
    print("=== Achievement Tracker System ===\n")
    print(
        f"Player alice achievements: {alice}\n"
        f"Player bob achievements: {bob}\n"
        f"Player charlie achievements: {charlie}\n"
    )
    print("=== Achievement Analytics ===\n")
    print(
        f"All unique achievements: {ach}\n"
        f"Total unique ahievements: {len(ach)}\n"
    )
    rare = (alice.difference(bob, charlie) |
            bob.difference(alice, charlie) |
            charlie.difference(alice, bob))
    print(
        f"Common to all players: {alice.intersection(bob, charlie)}\n"
        f"Rare achievements (1 player): {rare}"
    )
    print(
        f"\nAlice vs Bob common: {alice.intersection(bob)}"
        f"\nAlice unique: {alice.difference(bob)}"
        f"\nBob unique: {bob.difference(alice)}"
    )


ft_achievement_tracker()
