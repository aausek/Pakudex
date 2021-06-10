# Developed by Ana Ausek - 06/09/2021
from pakuri import Pakuri
import os

def main():
    print('Welcome to Pakudex: Let''s Go!\n')
    printMenu()


def printMenu():
    print('Pakudex Main Menu\n \
-----------------\n \
1. List Pakuri\n \
2. Show Pakuri\n \
3. Add Pakuri\n \
4. Remove Pakuri\n \
5. Change Pakuri Level\n \
6. Exit\n')
    selection = input('What would you like to do?')
    menuSelection(selection);


def menuSelection(selection):

    # If 1 list pakuri
    if selection == '1':
        Operation('list')
    # If 2 show pakuri
    elif selection == '2':
        Operation('show')
    # If 3 add pakuri
    elif selection == '3':
        Operation('add')
    # If 4 remove pakuri
    elif selection == '4':
        Operation('remove')
    # If 5 change pakuri
    elif selection == '5':
        Operation('change')
    # If 6 print exit message and quit program
    elif selection == '6':
        print('Thanks for using Pakudex: Let''s Go! Bye!')
        exit()
    else:
        print('Unrecognized menu selection!\n')
        printMenu()

def Operation(oper):


# Set main()
if __name__ == '__main__':
    main()
