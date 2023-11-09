from msvcrt import getwch
import os
from typing import KeysView 
os.system ('cls')


def calc_me(x, y):
    return x + y


print(calc_me(2,2))



def my_name(x):
    return (x)

print(my_name("Nicklas"))




def calc_me2(x, y):
    return x + y

i = 0
while i < 10:
    print(calc_me2(1,2)) 
    i = i + 1





Names = ["Isak", "Isjak", "Isad", "Leonard"]
Keys = ["a", "r", "r"]

def Name_list():
    return Names

def add_name(new):
    Names.append(new)

def remove_name(remove):
    Names.pop(remove)

def edit_name(edit):
    Names[edit] = name

while True:
    Keys = getwch().lower()
    if Keys == "a":
        new = input("Nytt namn: ")
        add_name(new)
        print(Names())
    elif Keys == "r":
        remove = int(input("ta bort ett namn"))
        remove_name(remove-1)
        print(Names())
    elif Keys == "e":
        edit = int(input("Vilket namn vill du ändra?"))
        name = input("Skriv det nya ")

        





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

resultat = calc(x, y, op)
print("Svar", resultat)


