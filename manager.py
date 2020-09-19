from models import Schema
from service import ManagerService
import os

def main(password):
    os.system("cls")
    ManagerService().printAll()
    items = ManagerService().listItems()
    print(items)

    print("Choose your action: ")
    print("1 - add item")
    print("2 - delete item")
    print("3 - edit item")
    print("4 - clear all data")
    print("Press q to quit")
    choice = input()
    if choice == '1':
        ManagerService().add()
    if choice == '2':
        ManagerService().delete()
    if choice == '3':
        ManagerService().update()
    if choice == '4':
        ManagerService().clear()
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