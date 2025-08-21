# login_with_lock.py

users = {"alice": "pass123", "bob": "admin"}
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    try:
        username = input("Username: ")
        password = input("Password: ")

        if username not in users:
            raise KeyError("User does not exist.")

        if users[username] != password:
            raise PermissionError("Wrong password.")

        print("✅ Login successful!")
        break  # Exit loop on successful login

    except KeyError as ke:
        print("Login Error:", ke)

    except PermissionError as pe:
        print("Login Error:", pe)

    finally:
        attempts += 1
        print(f"Login attempt {attempts} of {MAX_ATTEMPTS} logged.\n")

    if attempts == MAX_ATTEMPTS:
        print("⛔ Too many failed attempts. Account locked.")
