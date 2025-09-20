import random
import string

def generate_password(length, use_special_chars):
    letters = string.ascii_letters      
    digits = string.digits              
    symbols = string.punctuation if use_special_chars else ''
    
    all_chars = letters + digits + symbols
    
    # minimum one digit
    password = [random.choice(letters), random.choice(digits)]
    
    if use_special_chars:
        # Ensure at least one symbol
        password.append(random.choice(symbols))
    
    # For completing the full password
    if length < len(password):
        length = len(password)
    password += random.choices(all_chars, k=length - len(password))
    
    random.shuffle(password)
    return ''.join(password)

# User input
length = int(input("Enter desired password length: "))
special_choice = input("Include special characters? (yes/no): ").strip().lower()
use_special_chars = True if special_choice == 'yes' else False

# Generate and display password
password = generate_password(length, use_special_chars)
print("Generated Password:", password)
