import sys

def input_validator(input_prompt: str):
    """Handles user input and exits if 'exit' or 'ex' is entered."""
    user_input = input(input_prompt).strip().lower()

    if user_input == "exit" or user_input == "ex" :
        print("\n🚪 Exiting the application... Goodbye! 👋")
        sys.exit(0)  # Exit the program safely
    else :
        return user_input