
import json
import os
from colors import bcolors

def clear_screen():
    os.system('cls')

def show_welcome_message():
    print(bcolors.GREEN + bcolors.UNDERLINE + "Välkommen till körkortstestet!")
    print(bcolors.PURPLE + "Tryck på 's' för att starta spelet." + bcolors.DEFAULT)
    while True:
        if input().strip().lower() == 's':
            break

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, "Provfrågor.json")

    with open(file_name, 'r', encoding='utf-8') as file:
        questions = json.load(file)

    Keys = ["a", "b", "c", "d"]
    correct_answers = 0
    incorrect_answers = []

    number = 1
    for question_data in questions:
        clear_screen()
        print("\nFråga", number, "", question_data["question"])
        option_index = 0
        for key in Keys:
            print(key + "", question_data[Keys[option_index]])
            option_index += 1

        answer = input("Ditt svar (a/b/c/d): ").strip().lower()
        correct_answer = Keys.index(question_data["key"].lower())

        if answer == Keys[correct_answer]:
            correct_answers += 1
        else:
            incorrect_answers.append((number, question_data["question"], Keys[correct_answer]))

        number += 1

    total_questions = len(questions)
    points = correct_answers / total_questions * 100

    clear_screen()
    print("\nPoäng:", points)
    if points >= 70:
        print(bcolors.GREEN + "Grattis, du är godkänd!" + bcolors.DEFAULT)
    else:
        print(bcolors.RED + "Du misslyckades, du blev inte godkänd." + bcolors.DEFAULT)

    if points < 100:
        print("\nDu missade följande frågor:")
        for number, question, correct_key in incorrect_answers:
            print(bcolors.RED + "Fråga", number, "", question)
            print("Rätt svar:", correct_key + bcolors.DEFAULT)
    
    print("\nDu svarade rätt på följande frågor:")
    for number, question_data in enumerate(questions):
        correct_answer = Keys.index(question_data["key"].lower())
        if number + 1 not in [i[0] for i in incorrect_answers]:
            print(bcolors.GREEN + "Fråga", number + 1, "", question_data["question"])
            print("Rätt svar:", Keys[correct_answer] + bcolors.DEFAULT)

if __name__ == "__main__":
    clear_screen()
    show_welcome_message()
    main()
