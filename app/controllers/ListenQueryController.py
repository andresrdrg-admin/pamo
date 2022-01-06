from app.libs.Database import DB
from app.models.ListenQuery import ListenQuery
import time

class ListenQueryController():
    def __init__(self, query) -> None:
        listenquery = ListenQuery()
        listenquery.query = query
        listenquery.timecreated = time.time()
        created = listenquery.save()
        print(True if created != False else False)
