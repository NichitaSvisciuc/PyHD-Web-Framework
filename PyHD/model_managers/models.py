from peewee import *

class Query:

	@staticmethod
	def all_objects(cls_object):
		query_items = [item for item in cls_object.select()]
		return query_items