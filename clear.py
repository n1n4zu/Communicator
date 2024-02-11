from platform import system
from os import system as system2


def Clear():
    if system() == "Windows":
        system2("cls")

    elif system() == "Linux" or system() == "Unix":
        system2("clear")
