import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")

    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play?: "))

    for round in range(1, rounds + 1):
        print(f"\nRound {round}")

        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose from rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chooses:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("\nGame Over!")
    print(f"Final Score: You - {user_score}, Computer - {computer_score}")

    if user_score == computer_score:
        print("It's a tie!")
    elif user_score > computer_score:
        print("Congratulations! You win the game!")
    else:
        print("Sorry! Computer wins the game!")

if __name__ == "__main__":
    main()
