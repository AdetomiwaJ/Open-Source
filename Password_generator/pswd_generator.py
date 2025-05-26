import random
import string

ans = input("Do you want to generate a password? (yes/y): ")

if ans.lower() in ["yes", "y"]:
    while True:
        ch = input("What's the password length? How many characters do you want: ")
        if ch.isdigit():
            ch = int(ch)
            break
        else:
            print("Please enter a valid integer.")

    print("Password length selected:", ch)

    try:
        strength = int(input(
            "1 - Weak\n"
            "2 - Medium\n"
            "3 - Strong\n"
            "Select password strength: "
        ))

        if strength not in [1, 2, 3]:
            print("Invalid selection.")
        else:
            print(f"You selected option {strength}")

            if strength == 1:
                chars = string.ascii_lowercase
            elif strength == 2:
                chars = string.ascii_letters + string.digits
            elif strength == 3:
                chars = string.ascii_letters + string.digits + string.punctuation

            # Generate password
            password = ''.join(random.choice(chars) for _ in range(ch))
            print(f"\nGenerated password: {password}")

    except ValueError:
        print("Please enter a number (1, 2, or 3).")
else:
    print("Okay, no password will be generated.")
