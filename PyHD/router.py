from PyHD.exceptions import InexistentPath

class Path:

	""" This class specifies the structure of a path """

	__slots__ = ('func', 'path')

	def __init__(self, path: str, func):
		self.func = func
		self.path = path

	def match(self, _path):

		# function that is used to check whether a url route matches
		# that of the path.
		# Todo: Change to support dynamic urls like
		# /<int:id>/ just like django does so we can extract variables
		# from urls. 
		# Tip: You may need to learn regular expressions to match that

		if self.path == _path:
			return True
		return False

class Router:

	""" Holds all urls that we provide in a list and searches for matching one """

	__slots__ = [
		'routes',
	]

	def __init__(self, routes: list=None):
		self.routes = list(routes) if routes else []

	def add_route(self,  _path: Path):
		self.routes.append(_path)
		return True

	def get_route(self, path):

		for route in self.routes:
			if route.path == path:
				return route.func

		raise InexistentPath('You must provide a valid and existent url')