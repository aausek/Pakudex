# Developed by Ana Ausek - 06/09/2021
from pakuri import Pakuri
import os


def main():
    print("Welcome to Pakudex: Let's Go!\n")
    printMenu()

def printMenu():
    print('Pakudex Main Menu')
    print('-----------------')
    print('1. List Pakuri')
    print('2. Show Pakuri')
    print('3. Add Pakuri')
    print('4. Remove Pakuri')
    print('5. Change Pakuri Level')
    print('6. Exit')
    
    selection = input('What would you like to do? ')
    menuSelection(selection)


def menuSelection(selection):
    pkList = Pakuri.pkList
    # If 1 list pakuri
    if selection == '1':
        List(pkList)
        printMenu()
    # If 2 show pakuri
    elif selection == '2':
        Show(pkList)
        printMenu()
    # If 3 add pakuri
    elif selection == '3':
        Add(pkList)
        printMenu()
    # If 4 remove pakuri
    elif selection == '4':
        Remove(pkList)
        printMenu()
    # If 5 change pakuri
    elif selection == '5':
        changeLevel(pkList)
        printMenu()
    # If 6 print exit message and quit program
    elif selection == '6':
        print("\nThanks for using Pakudex: Let's Go! Bye!")
        exit(0)
    else:
        print('\nUnrecognized menu selection!\n')
        printMenu()

def printPk(pkList):
    print("\nPakuri in Pakudex:")
    for count, pakuri in enumerate(pkList, 1):
        print(f"{count}. {pakuri.name} ({pakuri.species}, level {pakuri.level})")
    print("")

def nameCheck(nameInput, pkList):
    for pk, pakuri in enumerate(pkList):
        if nameInput == pakuri.name:
            return pakuri, pk
    return False, False

def levelCheck(inputMsg):
    temp = None
    xLevel = True
    while xLevel:
        temp = input(inputMsg)
        try:
            temp = int(temp)
            if temp < 0:
                print('Level cannot be negative.')
            elif temp > 50:
                print('Maximum level for Pakuri is 50.')
            else:
                xLevel = False
        except ValueError:
            print('Invalid level!')
    return temp

def List(pkList):
    if pkList:
        printPk(pkList)
    else:
        print('\nNo Pakuri in Pakudex yet!\n')

def Show(pkList):
    nameInput = input('\nEnter the name of the Pakuri to display: ')
    pk, pakuri = nameCheck(nameInput, pkList)
    if pk:
        print(f'\nName: {pk.name}\n'
            f'Species: {pk.species}\n'
            f'Level: {pk.level}\n'
            f'CP: {pk.cp}\n'
            f'HP: {pk.hp}\n')
    else:
        print('Error: No such Pakuri!\n')


def Add(pkList):
    print('\nPakuri Information\n\
------------------')
    nameInput = input('Name: ')
    if nameCheck(nameInput, pkList)[0]:
        print('Error: Pakudex already contains this Pakuri!\n')
    else:
        speciesInput = input('Species: ')
        levelInput = levelCheck('Level: ')
        pk = Pakuri(nameInput, speciesInput, levelInput)
        pkList.append(pk)
        pkList.sort(key=lambda x: x.name, reverse=False)
        print(f'\nPakuri {pk.name} ({pk.species}, level {pk.level}) added!\n')

def Remove(pkList):
    nameInput = input('\nEnter the name of the Pakuri to remove: ')
    pk, pakuri = nameCheck(nameInput, pkList)
    if pk:
        del pkList[pakuri]
        print(f'Pakuri {pk.name} removed.\n')
    else:
        print('Error: No such Pakuri!\n')    

def changeLevel(pkList):
    nameInput = input('\nEnter the name of the Pakuri to change: ')
    pk, pakuri = nameCheck(nameInput, pkList)
    if pk:
        level = levelCheck('Enter the new level for the Pakuri: ')
        print('')
        pkList[pakuri].set_level(level)
    else:
        print('Error: No such Pakuri!\n') 


# Set main()
if __name__ == '__main__':
    main()
