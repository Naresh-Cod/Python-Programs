def dictionary_attack(target_password, dictionary_file):
    try:
        with open(dictionary_file, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                guess = line.strip()

                print(f"Trying password: {guess}")

                if guess == target_password:
                    print(f"Password found: {guess}")
                    return True

        print("Password not found in the dictionary.")
        return False
    except FileNotFoundError:
        print(f"Dictionary file '{dictionary_file}' not found.")
        return False


# Target password to crack
target_password = input("Enter the password to crack: ")

# Path to the dictionary file
dictionary_file = "passwords.txt"

# Start the dictionary attack
dictionary_attack(target_password, dictionary_file)
