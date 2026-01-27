def crisis_response_demo():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        file = open("lost_archive.txt", 'r')
    except FileNotFoundError:
        print(
            "RESPONSE: Archive not found in storage matrix\n"
            "STATUS: Crisis handled, system stable\n"
        )
    print("CRISIS ALERT: Attempting access to 'classified_data.txt'...")
    try:
        with open("classified_data.txt", 'a+') as file:
            file.write("writing without permission")
    except PermissionError:
        print(
            "RESPONSE: Security protocols deny access\n"
            "STATUS: Crisis handled, security maintained\n"
        )
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open("standard_archive.txt", 'r') as file:
        print(
        f"SUCCESS: Archive recovered - ''{file.read()}''\n"
        "STATUS: Normal operations resumed\n"
    )
    print("All crisis scenarios handled successfully. Archives secure.")

crisis_response_demo()