import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a secure password based on the chosen options."""
    
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.<>/?"
    
    if not characters:
        raise ValueError("No characters available to generate password.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Secure Password Generator 🔐")
    try:
        length = int(input("Password length (default 12): ") or 12)
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\n✅ Your generated password is:\n{pwd}")
    except ValueError as e:
        print(f"❌ Error: {e}")
