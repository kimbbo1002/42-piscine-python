def create_file() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    try:
        open(file_name, 'r')
        print(f"{file_name} already exists, writing aborted.\n")
    except FileNotFoundError:
        print(f"Initializing new storage unit: {file_name}")
        with open(file_name, "a+") as file:
            print(f"Storage unit created successfully...\n")
            data = (
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n"
            )
            print("Inscribing preservation data...")
            file.write(data)
            file.close()
        with open(file_name, 'r') as file:
            print(file.read())
            file.close()
        print(
            "Data inscription complete. Storage unit sealed.\n"
            f"Archive '{file_name}' ready for long-term preservation."
        )

create_file()