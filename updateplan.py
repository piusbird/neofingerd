# upsertplan UPSERT a plan file for a type 255 (normal entity)

import sys
import sqlite3
import random 
import string
import pickle
from settings import *
from utypes import *


sqls = """
INSERT OR REPLACE INTO lusers (unix_name, type, data) VALUES (?,?,?) 
"""
def type_ff():
    db = sqlite3.connect(DBNAME)
    c = db.cursor()
    planfile = open(sys.argv[2]).read()

    c.execute(sqls, (sys.argv[1], PLAINTEXT_TYPE, planfile))
    db.commit()
    db.close()
    sys.exit(0)


def rndname(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def type_b():
    db = sqlite3.connect(DBNAME)
    c = db.cursor()
    planfile = open(sys.argv[1]).read()

    c.execute(sqls, (rndname(), BANNER_TYPE, planfile))
    db.commit()
    db.close()
    sys.exit(0)

def type_4c():
    db = sqlite3.connect(DBNAME)
    c = db.cursor()
    name = input("Name of dynamic user:")
    print("Enter Dynamic command to use with full paths to all files\n")
    raw = sys.stdin.readline().strip().split(' ')
    planfile = pickle.dumps(raw)

    c.execute(sqls, (name, DYN_TYPE, planfile))
    db.commit()
    db.close()
    sys.exit(0)
            

if __name__ == '__main__':
    if len(sys.argv ) == 3:
        type_ff()
    elif len(sys.argv) == 2:
        type_b()
    elif len(sys.argv) == 1:
        type_4c()
    else:
        print("Error unknown invocation\n")
        sys.exit(1)

