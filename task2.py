import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        return "Error! No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator")
    while True:
        try:
            length = int(input("Enter password length: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()