from models import Schema
from service import ManagerService
import os

def main(password):
    os.system("cls")
    MS = ManagerService(password)
    if MS.printAll() == False:
        return False

    print("")
    print("Choose your action: ")
    print("1 - add item")
    print("2 - delete item")
    print("3 - edit item")
    print("4 - clear all data")
    print("Press q to quit")
    choice = input()
    if choice == '1':
        MS.add()
    if choice == '2':
        MS.delete()
    if choice == '3':
        MS.update()
    if choice == '4':
        MS.clear()
    if choice == 'q' or choice == 'Q':
        return False
    return True

    #TODO:
    #Implement encryption in db

if __name__ == "__main__":
    Schema()
    password = input("Enter password: ")
    while(main(password)):
        pass