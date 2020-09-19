import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('manager.db')
        self.createManagerTable()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def createManagerTable(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Manager"(
            id INTEGER PRIMARY KEY,
            App TEXT,
            Username TEXT,
            Password TEXT,
            Comments text
        );
        """
        self.conn.execute(query)
        print("ManagerTable created")

class ManagerModel:
    TABLENAME = "Manager"

    def __init__(self):
        self.conn = sqlite3.connect('manager.db')
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def get_by_id(self, _id):
        where_clause = f" WHERE id={_id}"
        return self.list_items(where_clause)

    #Add items to table
    def add(self, params):
        query = f'insert into {self.TABLENAME}' \
                f'(App, Username, Password, Comments)' \
                f'values ("{params.get("App")}","{params.get("Username")}",' \
                f'"{params.get("Password")}","{params.get("Comments")}")'
        result = self.conn.execute(query)
        #return self.get_by_id(result.lastrowid)

    def list_items(self, where_clause = ""):
        query = f"SELECT * FROM {self.TABLENAME}" + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        #print(result_set)
        
        #result = [{column: row[i]
        #           for i, column in enumerate(result_set[0].keys())}
        #            for row in result_set]

        return result_set
    
    #Delete items
    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} "\
                f"WHERE id = {item_id}"
        print(query)
        self.conn.execute(query)
        return self.list_items()


    #Clear all data
    def clear(self):
        query = f"DELETE from {self.TABLENAME}"
        self.conn.execute(query)

    #TODO:    
    #Edit item
