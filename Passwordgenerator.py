import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine character pools
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols

    if len(all_characters) == 0:
        raise ValueError("No character types selected! Please include at least one type of character.")

    # Ensure password meets all criteria by including at least one of each selected type
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase_letters))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password length with random choices from all characters
    remaining_length = length - len(password)
    password.extend(random.choices(all_characters, k=remaining_length))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# User input and usage
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
