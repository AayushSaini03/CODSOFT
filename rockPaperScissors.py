import random

def get_user_choice():
    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter the number of your choice: ")
        if choice in ('1', '2', '3'):
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.randint(1, 3)

def display_choice(choice):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You chose: {choices[choice - 1]}")

def display_result(player_choice, computer_choice):
    choices = ["Rock", "Paper", "Scissors"]
    player = choices[player_choice - 1]
    computer = choices[computer_choice - 1]

    print(f"Computer chose: {computer}")

    if player_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif (
        (player_choice == 1 and computer_choice == 3)
        or (player_choice == 2 and computer_choice == 1)
        or (player_choice == 3 and computer_choice == 2)
    ):
        print("You win this round!")
        return "player"
    else:
        print("Computer wins this round!")
        return "computer"

def main():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = get_user_choice()
        computer_choice = get_computer_choice()

        display_choice(player_choice)
        round_winner = display_result(player_choice, computer_choice)

        if round_winner == "player":
            player_score += 1
        elif round_winner == "computer":
            computer_score += 1

        print(f"Player Score: {player_score}  Computer Score: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final Score: Player {player_score} - Computer {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
