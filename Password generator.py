rs that will be used in the password (letters, digits, and special characters)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password from the pool of characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        # Get user input for the password length
        length = input("Enter desired password length (minimum 6): ")
        
        # Ensure the input is a valid number and meets the minimum length requirement
        if length.isdigit() and int(length) >= 6:
            length = int(length)
            break
        else:
            print("Please enter a valid number greater than or equal to 6.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("\nPassword generated successfully!")
    print(f"Generated Password: {password}\n")
    
    # Ask the user if they want to generate another password or exit
    while True:
        user_choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if user_choice == 'yes':
            main()  # Restart the process
            break
        elif user_choice == 'no':
            print("Thank you for using the Password Generator! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
# Run the program
main()
