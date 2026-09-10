
import random

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (snake/water/gun): ").lower()
        if user_input in ["snake", "water", "gun"]:
            return user_input
        else:
            print("Invalid choice! Please enter snake, water, or gun.")

def check_winner(user_choice, computer_choice):
    # Matrix (list of lists) representing result of user_choice vs computer_choice
    # Rows and columns are in order: snake, water, gun
    # 0 = Tie, 1 = User wins, -1 = Computer wins
    options = ["snake", "water", "gun"]

    result_matrix = [
        [0, -1, 1],   # snake vs [snake, water, gun]
        [1, 0, -1],   # water vs [snake, water, gun]
        [-1, 1, 0]    # gun   vs [snake, water, gun]
    ]

    user_index = options.index(user_choice)
    computer_index = options.index(computer_choice)

    result = result_matrix[user_index][computer_index]

    if result == 0:
        return "It's a tie!"
    elif result == 1:
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Snake, Water, Gun!")
    print("Rules: Gun beats Snake, Snake beats Water, Water beats Gun.\n")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = check_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
