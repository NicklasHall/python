import os
os.system('cls')

import  math


min_length=1.4 
length= float(input("Hur lång är du i meter?")) 
if length >=min_length:
    print("Du får åka:)")
elif length < min_length:
    print("Kortis du får inte åka väx lite isället")



print("Välkommen min vän") 
name =str(input("Namn: ")) 

while True:
    try:
        age =int(input("Ålder: ")) 
        break
    except:
        print("Skriv heltal")
    



while True:
    try:

        a1=float(input("hur lång är du i meter: "))
        b1=float(input("Hur myvket väger du kg: "))

        print(b1//(a1**2))  #Det här är en BMI räknare
        break
    except: 
        print("skriv med decimaler")




while True:

    try:
        radius = float(input("cirklens radie")) 
        print(radius*radius*math.pi)
        break
    except:
        print("Skriv siffror")





op = int(input(" vilket räknesätt vill du räkna med (1 = + 2 = - 3 = * 4 = /)"))
x = float(input("x: "))
y = float(input("y: "))

if op == 1:
    print(x + y)
elif op == 2:
    print(x - y)
elif op == 3:
    print(x * y)
elif op == 4:
    print(x / y)





import random


x = int(input("Hur många tärningar vill du ha?"))

for x in range(1,x+1):
    dice = random.randint(1, 6)
    print(dice)
