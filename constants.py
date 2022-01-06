import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
APP_DIR = "{}{}".format(ROOT_DIR, "/app")
EXTS_DB = "{}{}".format(APP_DIR, "/db/exts.db")