import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits

    if special_characters:
        characters += special

    password = ""

    password_eligible = False
    contain_number = False
    contain_special = False

    while not password_eligible or len(password) < min_length:
        random_character = random.choice(characters)
        password += random_character

        if random_character in digits:
            contain_number = True
        elif random_character in special:
            contain_special = True

        password_eligible = True

        if numbers:
            password_eligible = contain_number

        if special_characters:
            password_eligible = password_eligible and contain_special

    return password       


min_length = int(input("Enter the minimum length: "))
has_number = input("Contain numbers (y/n)? ").lower() == "y"
has_special = input("Contain special characters (y/n)? ").lower() == "y"

generated_password = generate_password(min_length, has_number, has_special)

print("The generated password is:", generated_password)

