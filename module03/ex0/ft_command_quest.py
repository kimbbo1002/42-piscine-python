import sys

def ft_command_quest() -> None:
    print("=== Command Quest ===")
    length = len(sys.argv)
    if length == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if length > 1:
        print(f"Arguments received: {length - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {length}")
