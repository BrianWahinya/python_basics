import os, re

def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def userInput():
    user_input = input("Please enter a valid value:\n")

    while not user_input:
        print("Error: Please input valid values")
        user_input = input("Input:\n")
    
    return user_input

def remove_special_characters(text):
    # Define a regular expression pattern to match special characters
    pattern = r'[^a-zA-Z0-9\s]'  # This pattern matches anything that is not a letter, digit, or whitespace

    # Use the sub() function from the re module to replace matched patterns with an empty string
    new_text = re.sub(pattern, '', text)

    return new_text