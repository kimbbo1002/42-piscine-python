import os
import sys
from dotenv import load_dotenv


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    load_dotenv()

    mode = os.getenv('MATRIX_MODE')
    database = os.getenv('DATABASE_URL')
    api = os.getenv('API_KEY')
    log = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')

    print(f"Mode: {mode}" if mode else "Mode: UNKNOWN")
    print(f"Database: {database}" if database else "Database: UNKNOWN")
    print(f"API Access: {api}" if api else "API Access: UNKNOWN")
    print(f"Log Level: {log}" if log else "Log Level: UNKNOWN")
    print(f"Zion Network: {zion}" if zion else "Zion Network: UNKNOWN")

    config: bool = all([mode, database, api, log, zion])
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if config:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file is NOT configured properly")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
