import sys

def print_to_stderr(*args) -> None:
    print(*args, file=sys.stderr)


def print_to_streams() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_id = input("Input Stream active. Enter archivist ID: ")
    stat_rep = input("Input Stream active. Enter status report: ")
    print(f"\n[STANDARD] Archive status from {arch_id}: {stat_rep}")
    print_to_stderr(
        "[ALERT] System diagnostic: Communication channels verified"
    )
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")

print_to_streams()