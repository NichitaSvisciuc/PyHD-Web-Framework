""" Here all migrations on database are aplied """
import sys
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework/PyHD/model_managers')
from migration_not_needed_class_names import packages

import models
import inspect

sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')
from settings import DATABASE

# Takes all classes from models to make tables from them
clsmembers = inspect.getmembers(models, inspect.isclass)

# Model Class objects
classes = [x for x in clsmembers if x[0] not in packages]


def create_column(column_class_object) -> None:
	db.create_tables([column_class_object], safe=True)


def print_all_tables(db) -> None:
	tables = db.get_tables()

	if len(tables) != 0:
		print('\nAll current tables : ')
		tables = [''.join(x).capitalize() for x in tables]
		print(', '.join(tables))
	else:
		print('\nYou dont have any table yet')


if __name__ == '__main__':
	# Makes tables in SQL Database
	with models.db as db:
		open(DATABASE, "w").close()
		tables = db.get_tables()

		# Updates and creates tables
		for klass in classes:

			if not klass[0].lower() in tables:
				create_column(klass[1])
				print(f'- Table created/updated for {klass[0]}')

		print_all_tables(db)