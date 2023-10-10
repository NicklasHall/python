import os   
import random
os.system("cls")


from colors import bcolors


print(bcolors.RED + "Välkommen till Gissa talet gissa ett tal mellan 1-100\n")

while True:
    secret_number=random.randint(1,100)
    lives=7

    while True:
        try:
            guess=int(input("Gissa på du bara"))
            if guess == secret_number:
                print("Grattis du gissade rätt")
                break
            elif guess > secret_number:
                print("Gissa på ett Lägre")
                
            elif guess < secret_number:
                print("Gissa på ett högre tal")
        except: 
            print("Skriv med tal inte bokstäver")        

        