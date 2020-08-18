# upsertplan UPSERT a plan file for a type 255 (normal entity)

import sys
import sqlite3
import random 
import string
import pickle
from settings import DBNAME
from utypes import *
import click


sqls = """
INSERT OR REPLACE INTO lusers (unix_name, type, data) VALUES (?,?,?) 
"""
delete_sqls = "DELETE FROM lusers WHERE unix_name='?';"

@click.group()
def cli():
    pass

@click.command()
@click.argument('unixname')
@click.argument('planfile')
def luseradd(unixname, planfile):
    db = sqlite3.connect(DBNAME)
    c = db.cursor()
    

    c.execute(sqls, (unixname, PLAINTEXT_TYPE, planfile))
    db.commit()
    db.close()
    click.echo("user added!")


def rndname(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@cli.command()
@click.argument('planfile')
def banner(planfile):
    db = sqlite3.connect(DBNAME)
    c = db.cursor()

    c.execute(sqls, (rndname(), BANNER_TYPE, planfile))
    db.commit()
    db.close()
    click.echo("banner will appear in rotation")

@cli.command()
@click.argument("name")
@click.argument("cmd")
def cgiadd(name,cmd):
    db = sqlite3.connect(DBNAME)
    c = db.cursor()
    raw = cmd.strip().split(' ')
    planfile = pickle.dumps(raw)

    c.execute(sqls, (name, DYN_TYPE, planfile))
    db.commit()
    db.close()
    click.echo("Please test your cgi")
            
def luserdel(name):
    pass


cli.add_command(luseradd)
if __name__ == '__main__':
    cli()