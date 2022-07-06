""" Here all migrations on database are aplied """
import sys
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework/')
from PyHD.model_managers.migration_not_needed_class_names import packages

import models
import inspect

sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')
from settings import DATABASE

# Takes all classes from models to make tables from them
clsmembers = inspect.getmembers(models, inspect.isclass)

# Model Class objects
classes = [x for x in clsmembers if x[0] not in packages]


def create_tables(column_class_object: list) -> None:
	db.create_tables(column_class_object, safe=True)


def print_tables(tables: list) -> None:
	""" Prints all current tables """
	if len(tables) > 0:
		curent_tables = [x.capitalize() for x in tables]
		print(', '.join(curent_tables))
	else:
		print('You dont have any tables created yet')


if __name__ == '__main__':
	# Makes tables in SQL Database
	try:
		with DATABASE as db:

			tables = db.get_tables()

			# Updates and creates tables
			for klass in classes:

				if not klass[0].lower() in tables:
					create_tables([klass[1]])
					print(f'- Table created for {klass[0]}')
				else:
					db.drop_tables([klass[1]])
					create_tables([klass[1]])
					print(f'- Table {klass[0]} updated')

			# Deletes a table if script detects that it removed from models.py
			class_names_lower = [x[0].lower() for x in classes]

			for table in tables:
				if table not in class_names_lower:
					db.execute_sql(f'DROP TABLE {table}')
					print(f'- Table {table.capitalize()} deleted')

			# If u want to see all your current tables decoment function below,
			# or use 'print_tables' anywhere you need
			""" print_tables(db.get_tables()) """
	except ValueError:
		print('Set your database')
