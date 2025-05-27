import random
import time
import string
import secrets

def random_generate():
    print(
        "_________________________________________________________________________\nSIMPLE PASSWORD GENERATOR\n_________________________________________________________________________\nRandom Password Generator\n_________________________________________________________________________\n"
    )

    try:
        num_chars = int(
            input(
                "Please enter number of characters that must be present (default 4): "
            )
        )

        if num_chars < 4:
            print(
                "Number of characters must be at least 4. Setting to default value of 4."
            )
            num_chars = 4
        else:
            print(f"Number of characters set to {num_chars}.")
    except:
        print("Setting number of characters to default value of 4.")
        num_chars = 4

    def pick_char(chars):
        return random.choice(chars)

    alphabets_caps = string.ascii_uppercase
    alphabets_low = string.ascii_lowercase
    special_chars = string.punctuation
    numbers = string.digits

    password = ""

    for i in range(num_chars):
        if i % 4 == 0:
            password += pick_char(alphabets_caps)
        elif i % 4 == 1:
            password += pick_char(alphabets_low)
        elif i % 4 == 2:
            password += pick_char(special_chars)
        else:
            password += pick_char(numbers)

    print(f"Password: {password}")


def web_generate():
    print(
        "_________________________________________________________________________\nSIMPLE PASSWORD GENERATOR\n_________________________________________________________________________\nWebsite Password Generator\n_________________________________________________________________________\n"
    )
    try:
        print("Enter the website name without https:// (e.g., example.com): ")
        website = str(input()).strip()

        if not website:
            print("Website name cannot be empty. Exiting.")
            return
        else:
            print(f"Website name set to: {website}")

        password = ""
        for i in range(3):  
            password += chr(ord(website[i - 1]) - 1) if i < len(website) else "x"

        if len(password) >= 3:
            password = password[:2] + password[2].upper() + password[3:]

        password += str(len(website)) + "!"
        password += str(random.randint(1000, 9999))
        password += random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

        print(
            f"Generated password for {website}: {password} \n \n Do you want to increase complexity? (y/n)"
        )
        choice = input().strip().lower()

        if choice == "y":
            password += time.strftime("%Y%m%d%H%M%S")
            password += random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
            print(f"Complex password for {website}: {password}")
        elif choice == "n":
            print(f"Final password for {website}: {password}")
        else:
            print("Invalid choice. Exiting.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
def pseudo_random_generate():
    
    print(
        "_________________________________________________________________________\nSIMPLE PASSWORD GENERATOR\n_________________________________________________________________________\nPRNG - Pseudo-Random Password Generator\n_________________________________________________________________________\n"
    )
    
    try:
        num_chars = int(
            input(
                "Please enter number of characters that must be present (default 4): "
            )
        )

        if num_chars < 4:
            print(
                "Number of characters must be at least 4. Setting to default value of 4."
            )
            num_chars = 4
        else:
            print(f"Number of characters set to {num_chars}.")
    except:
        print("Setting number of characters to default value of 4.")
        num_chars = 4

    def pick_char(chars):
        return secrets.choice(chars)

    alphabets_caps = string.ascii_uppercase
    alphabets_low = string.ascii_lowercase
    special_chars = string.punctuation
    numbers = string.digits

    password = ""

    for i in range(num_chars):
        if i % 4 == 0:
            password += pick_char(alphabets_caps)
        elif i % 4 == 1:
            password += pick_char(alphabets_low)
        elif i % 4 == 2:
            password += pick_char(special_chars)
        else:
            password += pick_char(numbers)

    print(f"Password: {password}")

if __name__ == "__main__":
    print("Welcome to the Simple Password Generator!")
    print("Choose an option:")
    print("1. Random Password Generator")
    print("2. Website Password Generator")
    print("3. PRNG - Pseudo-Random Password Generator")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == "1":
        random_generate()
    elif choice == "2":
        web_generate()
    elif choice == "3":
        pseudo_random_generate()
    else:
        print("Invalid choice. Exiting.")
