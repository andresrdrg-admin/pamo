from app.libs.Database import DB
from app.models.ListenQuery import ListenQuery
import time

class ListenQueryController():
    def __init__(self, query, iduser, parler):
        self.parler = parler
        listenquery = ListenQuery()
        listenquery.query = query
        ListenQuery.iduser = (iduser if iduser != False else "")
        listenquery.timecreated = time.time()
        created = listenquery.save()
        self.query = listenquery

    def validateQuery(self):
        if "salir" in self.query.query and "aplicación" in self.query.query:
            return "exit"
        elif "instalar" in self.query.query:
            return ("Parece que deseas instalar un módulo. ¿Cómo se llama el módulo?")
        else:
            return ("No instalaras un módulo")
