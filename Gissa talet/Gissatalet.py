import os
import random
from colors import bcolors

os.system("cls")

print(bcolors.RED + "Välkommen till Gissa talet! Gissa ett tal mellan 1-100\n")

while True:
    secret_number = random.randint(1, 100)
    lives = 7

    while lives > 0:
        try:
            guess = int(input("Gissa på du bara: "))
            if guess == secret_number:
                print("Grattis! Du gissade rätt.")
                break
            elif guess > secret_number:
                print("Gissa på ett lägre tal.")
            elif guess < secret_number:
                print("Gissa på ett högre tal.")
            lives -= 1
            print(f"Du har {lives} liv kvar.")
        except ValueError: # valde att leta själv och använda mig av valueError istället för det vi har lärt oss för att det var lättare tyckte jag 
            print("Skriv med tal, inte bokstäver.")

    if lives == 0:
        print(f"Tyvärr, du har inga försök kvar. Det hemliga talet var {secret_number}.")

    play_again = input("Vill du spela igen? (ja/nej): ").lower()
    if play_again != 'ja':
        break
    else:
        os.system("cls")


        