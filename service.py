from models import ManagerModel
from encryption import Crypto

class ManagerService:
    def __init__(self, password):
        self.crypto = Crypto(password)
        self.model = ManagerModel()
    
    def add(self):
        App = self.crypto.EncryptString(input("App/Webpage name: "))
        Username = self.crypto.EncryptString(input("Username: "))
        Password = self.crypto.EncryptString(input("Password: "))
        Comments = self.crypto.EncryptString(input("Comments: "))
        params = {"App": App, "Username": Username, \
            "Password": Password, "Comments": Comments}

        return self.model.add(params)
    
    def delete(self):
        item_id = input("Input id to delete item: ")
        return self.model.delete(item_id)
    
    def listItems(self):
        #TODO:
        #Error handling if table doesnt exist
        response = self.model.list_items()
        return response
    
    def clear(self):
        return self.model.clear()

    #TODO
    def update(self):
        #TODO error handling
        item_id = int(input("Item id to edit: "))
        column = ""
        value = ""
        flag = False
        while(not flag):
            print("Which column you want to edit?")
            print("1 - App/Website")
            print("2 - Username")
            print("3 - Password")
            print("4 - Comments")
            choice = input()
            if choice == '1':
                flag = True
                column = "App"
            if choice == '2':
                flag = True
                column = "Username"
            if choice == '3':
                flag = True
                column = "Password"
            if choice == '4':
                flag = True
                column = "Comments"
            if(not flag):
                print("Wrong input")

        value = input(f"Enter new {column} value: ")
        encrypted_value = self.crypto.EncryptString(value)
        params = [column, value]    
        return self.model.update(item_id, params)
    
    def printAll(self):
        response = self.listItems()
        id = "Id"
        App = "App/Website"
        Username = "Username"
        Password = "Password"
        Comment = "Comments"
        for i in range(len(response)+1):
            print(str(id).ljust(5) + App.ljust(25) + Username.ljust(20) + Password.ljust(18) + Comment)
            if i == 0:
                print("==========================================================================================")
            if i < len(response):
                item = response[i]
                id = item[0]
                App = self.crypto.DecryptString(item[1])
                Username = self.crypto.DecryptString(item[2])
                Password = self.crypto.DecryptString(item[3])
                Comment = self.crypto.DecryptString(item[4])

            
