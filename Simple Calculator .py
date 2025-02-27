# Simple Calculator

def perform_operation(num1, num2, operation):
    """Perform the selected arithmetic operation."""
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."

def show_menu():
    """Display the operation menu."""
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def calculator():
    """Main function for running the calculator."""
    print("Welcome to the Simple Calculator")

    while True:
        # Input for numbers
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Show operation menu and get user choice
        show_menu()
        try:
            operation = int(input("Enter the number corresponding to the operation: "))
        except ValueError:
            print("Invalid input! Please choose a valid operation number.")
            continue

        # Perform the operation and display result
        result = perform_operation(num1, num2, operation)
        print(f"\nResult: {result}")

        # Ask if user wants to continue
        continue_choice = input("\nWould you like to perform another operation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thank you for using the calculator! Goodbye.")
            break

# Run the calculator
calculator()

