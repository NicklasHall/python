# BÄSTAVAN.py: En bästa vän lista

__author__  = "Nicklas Hall"
__version__ = "1.0.0"
__email__   = "Nicklas.hall@elev.ga.ntig.se"

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
    Names.pop(remove - 1)

def edit_name(index, name):
    Names[index - 1] = name

while True:
    print_menu()
    choice = getwch()


    if choice == "1":
        print_names()
    elif choice == "2":
        new = input("Nytt namn: ")
        add_name(new)
        print_names()
    elif choice == "3":
        print_names()
        remove = int(input("Vilket nummer vill du ta bort? "))
        remove_name(remove)
        print_names()
    elif choice == "4":
        print_names()
        edit = int(input("Vilket nummer vill du ändra? "))
        name = input("Skriv det nya namnet: ")
        edit_name(edit, name)
        print_names()
    elif choice == "5":
        break
    else:
        print("Ogiltigt val. Försök igen.")
