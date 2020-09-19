from models import ManagerModel

class ManagerService:
    def __init__(self):
        self.model = ManagerModel()
    
    def add(self):
        App = input("App/Webpage name: ")
        Username = input("Username: ")
        Password = input("Password: ")
        Comments = input("Comments: ")
        params = {"App": App, "Username": Username, \
            "Password": Password, "Comments": Comments}

        return self.model.add(params)
    
    def delete(self):
        #TODO:
        #showAll(listItems())
        print("\n")
        item_id = input("Input id to delete item: ")
        return self.model.delete(item_id)
    
    def listItems(self):
        #TODO:
        #Error handling if table doesnt exist
        response = self.model.list_items()
        return response
    
    def clear(self):
        return self.model.clear()

    def ShowAll():
        pass

    #TODO
    #def update(self, item_id, params):
    #   return self.model.update(item_id, params)
