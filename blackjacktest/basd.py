import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate and return the total value of a hand of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack (special case)
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare_scores(player_score, computer_score):
    """Compare player's and computer's scores and determine the winner."""
    if player_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose! Computer has a Blackjack."
    elif player_score == 0:
        return "You win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Function to play the Blackjack game."""
    money = 100  # Starting money
    while True:
        print(f"Your current money: ${money}")
        bet = int(input("Place your bet: $"))
        if bet > money:
            print("You cannot bet more money than you have. Try again.")
            continue

        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                another_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
                if another_card == 'y':
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        result = compare_scores(user_score, computer_score)
        print(result)

        if result == "You win!" or result == "You win with a Blackjack!":
            money += bet
        elif result != "It's a draw!":
            money -= bet

        play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
        if play_again != 'y':
            break

# Run the game
play_game()
