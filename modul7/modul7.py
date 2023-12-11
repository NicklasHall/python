import os,time 
from colors import bcolors

os.system('cls')


def calc(x, y, op):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y
     

op = input("ange räkne sätt(+, -, *, /): ")
x = float(input())
y = float(input())
print("calculating...")

resultat = calc(x, y, op)
time.sleep( 4 )
print("Svar", bcolors.RED + str (resultat))






