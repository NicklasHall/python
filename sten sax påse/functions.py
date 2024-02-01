import random

def decide_winner(user_choice, ai_choice):
    outcomes = {
        ('R', 'S'): 'win',
        ('S', 'P'): 'win',
        ('P', 'R'): 'win',
        ('S', 'R'): 'loss',
        ('P', 'S'): 'loss',
        ('R', 'P'): 'loss',
    }

    if user_choice == ai_choice:
        return 'tie'
    elif (user_choice, ai_choice) in outcomes:
        return outcomes[(user_choice, ai_choice)]
    else:
        return 'loss'


def print_results(wins, losses, ties, total_rounds):
    print(f"\nResults: Wins - {wins}, Losses - {losses}, Ties - {ties}")
    print(f"Total Rounds Played: {total_rounds}")

def print_ascii_art(choice):
    rock_ascii = """
    _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/
"""
    paper_ascii = """
 __ __ __
|  |  |  |__
|¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/
"""
    scissors_ascii = """
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
"""

    if choice == 'R':
        print(rock_ascii)
    elif choice == 'P':
        print(paper_ascii)
    elif choice == 'S':
        print(scissors_ascii)
