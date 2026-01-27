def ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file}")
    try:
        vault = open(file)
        print("Connection established.,.\n")
        print(
            "RECOVERED DATA:\n"
            f"{vault.read()}"
        )
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")

ancient_text()