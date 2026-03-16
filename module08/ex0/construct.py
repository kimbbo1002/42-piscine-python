import sys
import os
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print(
            "\nMATRIX STATUS: You're still plugged in\n"
            f"\nCurrent Python: {sys.prefix}\n"
            "Virtual Environment: None detected\n"
            "\nWARNING: You're in the global environment!\n"
            "The machines can see everything you install"
            "\nTo enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
        )
    else:
        print(
            "\nMATRIX STATUS: Welcome to the construct\n"
            f"\nCurrent Python: {sys.base_prefix}\n"
            f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
            f"Environment Path: {sys.prefix}\n"
            "\nSUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting the global system.\n"
            "\nPackage installation path:\n"
            f"{site.getsitepackages()[0]}"
        )


if __name__ == "__main__":
    main()
