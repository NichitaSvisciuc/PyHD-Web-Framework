from pathlib import Path, os
from peewee import SqliteDatabase
from PyHD.middlewares.common_middlewares import *

BASE_DIR = Path(__file__).resolve().parent

# Your salt for passwords, keep it secret and do not share it to anyone
SECRET_KEY = 'kldgirkjoiwgrtdjyj-ethkmjpjdgsdsdg'

# Current name, change it on yours if your app hase another name
APP_NAME = 'project'

# Template directory, put your path if you need
TEMPLATES = os.path.join(BASE_DIR, f'{APP_NAME}\\templates')

# This is default database name, if you have another one just change it
DATABASE = SqliteDatabase('sqlite.db')

CORE_APP_DIRECTORY_URL = 'C:\\projects\\PyHDproject\\PyHD-Web-Framework'

# Here are all needed middlewares, you can create, import and add your own
MIDDLEWARES = [
    CommonMiddleware,
]

