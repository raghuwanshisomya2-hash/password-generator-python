import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "No character set selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("------ Password Generator ------")

length = int(input("Enter password length: "))

upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include numbers? (y/n): ").lower() == 'y'
symbols = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, upper, lower, digits, symbols)

print("\nGenerated Password:")
print(password)
