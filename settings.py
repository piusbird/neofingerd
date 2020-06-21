from dotenv import load_dotenv
import os
load_dotenv()
LOGFILE = os.getenv("NF_LOGFILE")
BASEDIR = os.getenv("NF_BASEDIR")
DBNAME = os.getenv("NF_DBNAME")
