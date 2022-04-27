from app.libs.Database import DB
import constants

class Modules():
    id = False
    name = False
    keywords = False
    timeinstalled = False

    def __init__(self) -> None:
        db = DB(constants.EXTS_DB)
        db.exec("CREATE TABLE IF NOT EXISTS mp_modules(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, keywords TEXT, timeinstalled INTEGER)")
    
    def save(self):
        db = DB(constants.EXTS_DB)
        query = "INSERT INTO mp_queries (`name`, `keywords`, `timeinstalled`) VALUES ('{}', '{}', {})".format(self.name, self.keywords, int(self.timeinstalled))
        return db.exec(query)

    def findAll(self):
        db = DB(constants.EXTS_DB)
        return db.exec("SELECT * FROM mp_modules")