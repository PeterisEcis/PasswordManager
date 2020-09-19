from models import Schema
from service import ManagerService

def main():
    ManagerService().add()
    items = ManagerService().listItems()
    print(items)
    ManagerService().delete()
    print("success!")
    ManagerService().clear()
    items = ManagerService().listItems()
    print(items)

    #TODO:
    #Implement encryption in db

if __name__ == "__main__":
    Schema()
    main()