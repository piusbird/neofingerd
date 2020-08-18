#!/usr/bin/env python3
# Note We're doing this using uscpi-tcp for inital testing
# We'll add the socket stuff later
import sqlite3
import os
import random
import pickle
import sys
import logging
import subprocess
from settings import *
DYN_TYPE = 76
BANNER_TYPE = 11
PLAINTEXT_TYPE = 255
CRLF = '\r\n'


def eat_pickle(sP):

    cmd = pickle.loads(sP)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return p.stdout.read().decode("ascii")


os.chdir(BASEDIR)
dbcon = None
try:
    dbcon = sqlite3.connect(DBNAME)
except Exception as e:
    sys.stdout.write(str(e))


def banner_query():

    from random import choice
    sqls = "SELECT data FROM lusers WHERE type=?"
    cur = dbcon.cursor()
    cur.execute(sqls, [BANNER_TYPE])
    bList = cur.fetchall()
    b = choice(bList)
    return b[0] + CRLF

def parse_and_query(uname):

    rv = "No such entity\r\n"
    if uname == '':
        banner_query()
    else:
        sqls = "SELECT type, data FROM lusers WHERE unix_name=?"
        cur = dbcon.cursor()
        cur.execute(sqls, [uname])
        data = cur.fetchone()
        if data:
            rv = eat_pickle(data[1])+CRLF if int(data[0]
                                                 ) == DYN_TYPE else data[1]+CRLF
    return rv


def info_query(uname):

    cur = dbcon.cursor()
    cur.execute("SELECT data FROM lusers WHERE unix_name=?", [uname])
    data = cur.fetchone()
    rv = data[0] + CRLF if data else "404 No such entity\r\n"
    return rv


def send_stdin():
    return sys.stdin.readline()


recv_query = send_stdin


def send_msg(x): return sys.stdout.write(str(x))

def entry():
    logging.basicConfig(filename=LOGFILE, filemode='w',
                        format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    line = recv_query()
    if line == "\r\n" or line == "\n":
        logging.warning("Query was blank sending banner")
        send_msg(banner_query())
    else:
        resp = parse_and_query(line.strip(CRLF))
        logging.warning("Query was %s sent %s", line.strip(
            CRLF), str(resp).strip(CRLF))
        send_msg(resp)
        sys.exit(0)

if __name__ == '__main__':
    entry()