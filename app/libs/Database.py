import sqlite3

class DB():
    def __init__(self, db) -> None:
        self.createConnection(db)
        
    def createConnection(self, db):
        self.conext = sqlite3.connect(db)
        self.shot = self.conext.cursor()

    def exec(self, query):
        result = self.shot.execute(query)
        self.conext.commit()
        self.conext.close()
        return result
