def secure_vault() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    with open("classified_data.txt", 'r') as file:
        print("Vault connection established with failsafe protocols\n")
        print(
            "SECURE EXTRACTION:\n"
            f"{file.read()}"
        )
    with open("security_protocols.txt", 'r') as file:
        print(
            "\nSECURE PRESERVATION:\n"
            f"{file.read()}"
        )
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")

secure_vault()
