"""
bästavänen.PY: Bästa vänner

__author__  = "Nicklas Hall"
__version__ = "1.0.0"
__email__   = nicklas.hall@elev.ga.ntig.se

"""

from msvcrt import getwch
import os

Names = ["Isak", "Isjak", "Isad", "Leonard"]

def print_menu():
    print("\n=== Mina bästa vänner ===")
    print("1. Visa lista")
    print("2. Lägga till namn")
    print("3. Ta bort namn")
    print("4. Ändra namn")
    print("5. Avsluta")

def print_names():
    print("Dina bästa vänner:")
    for i in range(len(Names)):
        print(f"{i + 1}. {Names[i]}")

def add_name(new):
    Names.append(new)

def remove_name(remove):
    if 1 <= remove <= len(Names):
        Names.pop(remove - 1)
    else:
        print("Ogiltigt nummer. Försök igen.")

def edit_name(index, name):
    if 1 <= index <= len(Names):
        Names[index - 1] = name
    else:
        print("Ogiltigt nummer. Försök igen.")

while True:
    print_menu()
    choice = getwch()

    if choice == "1":
        os.system("cls")  
        print_names()
    elif choice == "2":
        os.system("cls")  
        new = input("Nytt namn: ")
        add_name(new)
        print_names()
    elif choice == "3":
        os.system("cls")  
        print_names()
        remove = int(input("Vilket nummer vill du ta bort? "))
        remove_name(remove)
        print_names()
    elif choice == "4":
        os.system("cls")  
        print_names()
        edit = int(input("Vilket nummer vill du ändra? "))
        name = input("Skriv det nya namnet: ")
        edit_name(edit, name)
        print_names()
    elif choice == "5":
        break
    else:
        print("fel val. Försök igen.")
