import sys  
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')  

from PyHD.register_account_models.auth_models import User
from peewee import *
from settings import DATABASE

# Use in your Model a Meta class and 'database = db' will be as a field
# After Changing or writing a class run migrate.py file from project directory

# If u want to perform beautyfied standard queryes just import them from model_managers/models.py
# If u want to create a user u must import its model : from PyHD.register_account_models.auth_models import User
# and name your user class AuthUser, write a Meta class that will take the db in wich your users will be stored
# If u want to create another type of user just inherit it from User interface and use
# P.S('In this case you will not be able to use Normal user methods so write yours')

class Post(Model):

	title = CharField()

	class Meta:
		database = DATABASE

	def __str__(self):
		return self.title

class AuthUser(User):
	pass
