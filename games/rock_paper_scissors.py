from utils import clear_cmd
import random

clear_cmd()

input_dict = {
    "rock": "1",
    "paper": "2",
    "scissors": "3"
}
valid_values = [item for key_value in input_dict.items() for item in key_value]

def getComputerChoice():
    return random.choice(list(input_dict.values()))

def deriveInput():
    while True:
        user_input = input("Please enter Rock: 1, Paper: 2, Scissors: 3 or exit:\n").strip().lower()
        if user_input == "exit":
            return False
        
        if user_input not in valid_values:
            print("Error: Please input valid values")
            continue

        choice_user = None
        if user_input in input_dict.values():
            choice_user = user_input
        
        if user_input in input_dict:
            choice_user = input_dict[user_input]

        choice_comp = getComputerChoice()

        playGame(choice_comp, choice_user)

def playGame(choice_comp, choice_user):
    print(f"{choice_user} vs {choice_comp}")


if __name__ == "__main__":
    deriveInput()
