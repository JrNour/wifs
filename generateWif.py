import random

# Define Base58 characters excluding '0', 'O', 'I', 'l', 'A', 'B', 'C'
base58_chars = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

# Define first character options excluding 'A', 'B', 'C'
first_char_options = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

# File to store the passwords
output_file = "wifrandom.txt"

def generate_password():
    # First character from the restricted set
    first_char = random.choice(first_char_options)
    
    # Other characters from the full Base58 set
    other_chars = ''.join(random.choice(base58_chars) for _ in range(10))
    
    return first_char + other_chars

# Generate 1 million passwords
with open(output_file, 'w') as f:
    for _ in range(2_575_000):
        password = generate_password()
        f.write(password + '\n')

print("1 million passwords generated and saved to 'passwords.txt'.")
