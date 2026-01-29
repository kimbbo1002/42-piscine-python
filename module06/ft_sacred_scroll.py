import alchemy.elements

def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}\n"
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}\n"
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n"
    )
    print("Testing package-level acess (controlled by __init__.py):")
    print(
        f"alchemy.create_fire(): {alchemy.create_fire()}"
        f"alchemy.create_water(): {alchemy.create_water()}"
    )
    try:
        print(
            f"alchemy.create_earth(): {alchemy.create_earth()}"
        )
    except AttributeError:
        print(f"alchemy.create_earth(): AttributeError - not exposed")
    try: 
        print(
             f"alchemy.create_air(): {alchemy.create_air()}"
        )
    except AttributeError:
        print(f"alchemy.create_air(): AttributeError - not exposed")
    print(
        "\nPackage metadata:\n"
        f"Version: {alchemy.__version__}\n"
        f"Author: {alchemy.__author__}"
    )


if __name__ == "__main__":
    main()