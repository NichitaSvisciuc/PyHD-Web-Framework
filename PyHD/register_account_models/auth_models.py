import sys
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')
from settings import DATABASE, SECRET_KEY

from peewee import *

import hashlib
import random


class User(Model):
    id = AutoField()

    first_name = CharField(null=True)
    username = CharField()
    last_name = CharField(null=True)
    password = CharField()
    email = CharField(null=True)

    is_active = BooleanField(default=True, null=True)
    is_authenticated = BooleanField(default=False, null=True)
    is_staff = BooleanField(default=False, null=True)

    date_created = DateField()

    class Meta:
        database = DATABASE

    def __str__(self):
        return self.username

    @staticmethod
    def get_hexdigest(salt: str, raw_password: str) -> str:
        data = str(salt) + str(raw_password)
        return hashlib.sha1(data.encode('utf8')).hexdigest()

    @staticmethod
    def make_password(raw_password: str) -> str:
        salt = User.get_hexdigest(SECRET_KEY, str(random.random()))[:5]
        hsh = User.get_hexdigest(salt, raw_password)
        return '%s$%s' % (salt, hsh)

    @staticmethod
    def check_password(raw_password: str, enc_password) -> bool:
        salt, hsh = enc_password.split('$', 1)
        return hsh == User.get_hexdigest(salt, raw_password)
