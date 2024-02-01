import random
from functions import play_round, print_results, print_ascii_art

def main():
    wins, losses, ties, total_rounds = 0, 0, 0, 0

    while True:
        print("\nRock Paper Scissors Game:")
        print("Choose: (R)ock, (P)aper, (S)cissors, (Q)uit")

        user_choice = input("Your choice: ").upper()

        if user_choice == 'Q':
            break
        elif user_choice == 'N':
            wins, losses, ties, total_rounds = 0, 0, 0, 0
            print("New game started.")
            continue

        if user_choice not in ['R', 'P', 'S']:
            print("Invalid choice. Try again.")
            continue

        ai_choice = random.choice(['R', 'P', 'S'])
        print(f"AI chose: {ai_choice}")

        result = play_round(user_choice, ai_choice)

        if result == 'win':
            print("You win!")
            wins += 1
        elif result == 'loss':
            print("You lose!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        total_rounds += 1
        print_results(wins, losses, ties, total_rounds)
        print("\nYour choice:")
        print_ascii_art(user_choice)
        print("\nAI chose:")
        print_ascii_art(ai_choice)

if __name__ == "__main__":
    main()
