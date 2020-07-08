#!/home/jens/Schreibtisch/python_algorithmen_fuer_fahrzeugtechnik/pythonEnvironments/introEnv/bin/python3

"""This is the main file to start the application"""

from my_second_file import * # da das im aktuellen ordner ist, funktioniert das! (sofern eine __init__.py Datei im Ordner ist!)
import numpy as np


def print_hello_world():
    """
    Hello World print function
    """
    print("Hello World")


def main():
    """
    This is the main Method of the application
    """
    print("My test started")

    ten = my_function_1(5, 5)
    twenty = my_function_2(5, 5, 10)

    print("My test finished")


if __name__ == "__main__":
    main()
