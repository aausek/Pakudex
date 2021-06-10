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
    selection = int(input('What would you like to do? '))
    menuSelection(selection)


def menuSelection(selection):
    # If 1 list pakuri
    if selection == 1:
        # Operation('list')
        List()
        printMenu()
    # If 2 show pakuri
    # elif selection == 2:
    #     Operation('show')
    # # If 3 add pakuri
    elif selection == 3:
        Add()
        printMenu()
    # # If 4 remove pakuri
    # elif selection == 4:
    #     Operation('remove')
    # # If 5 change pakuri
    # elif selection == 5:
    #     Operation('change')
    # If 6 print exit message and quit program
    elif selection == 6:
        print('\nThanks for using Pakudex: Let''s Go! Bye!')
        exit(0)
    else:
        print('\nUnrecognized menu selection!\n')
        printMenu()


def List():
    obj = Pakuri.instances
    if obj:
        for num, ob in enumerate(obj):
            print(num + ' ' + ob.name + '(' + ob.species + ', level ' + ')')
    else:
        print('\nNo Pakuri in Pakudex yet!\n')


def Add():
    

# def Show()
# def Add()
# def Remove()
# def Change Level()


# Set main()
if __name__ == '__main__':
    main()
