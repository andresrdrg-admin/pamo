from app.libs.Database import DB
import constants

class ListenQuery():
    id = False
    query = False
    iduser = False
    timecreated = False

    def __init__(self) -> None:
        db = DB(constants.EXTS_DB)
        db.exec("CREATE TABLE IF NOT EXISTS mp_queries(id INTEGER PRIMARY KEY AUTOINCREMENT, query TEXT, iduser TEXT, timecreated INTEGER)")
    
    def save(self):
        db = DB(constants.EXTS_DB)
        query = "INSERT INTO mp_queries (`query`, `iduser`, `timecreated`) VALUES ('{}', '{}', {})".format(self.query, self.iduser, int(self.timecreated))
        return db.exec(query)

    def findAll(self):
        db = DB(constants.EXTS_DB)
        return db.exec("SELECT * FROM mp_queries")