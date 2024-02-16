import random
import string

def generate_password(length):
    # Define the characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice() to select characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    
    # Check if the specified length is valid
    if length <= 0:
        print("Invalid length. Please enter a positive integer.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if _name_ == "_main_":
    main()
