from app.libs.Database import DB
from app.models.ListenQuery import ListenQuery
import time

class ListenQueryController():
    def __init__(self, query, iduser = False) -> None:
        listenquery = ListenQuery()
        listenquery.query = query
        ListenQuery.iduser = (iduser if iduser != False else "")
        listenquery.timecreated = time.time()
        created = listenquery.save()
