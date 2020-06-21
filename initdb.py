import sqlite3
import os 
from settings import *

schema = open("schema.sql").read()
banner1 = open("banner1").read()
banner = open("banner").read()
os.chdir(BASEDIR)

db = sqlite3.connect(DBNAME)
c = db.cursor()
c.execute(schema)
db.commit()

uname = os.getenv("USER")

sqls = "INSERT INTO lusers (unix_name, type, data) VALUES (?,?,?)"

c.execute(sqls, (uname, 255, "Created this foolishness"))
c.execute(sqls, ("__b1__", 11, banner1))
c.execute(sqls, ('__b__', 11, banner))
db.commit()
db.close()
