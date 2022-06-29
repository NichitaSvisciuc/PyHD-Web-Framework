import sys
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')
from settings import MIDDLEWARES

from PyHD.exceptions import InexistentPath
from PyHD.request import Request
from PyHD.router import Router
from PyHD.response import Response, PageNotFound


class App:

	def __init__(self):
		self.router = Router()

	def set_routes(self, routes: list):
		""" takes a list of Paths and add them to the app's router's list of routes """
		for path in routes:
			self.router.add_route(path)

	def start_response(self, request):
		return request.start_response

	# Its the result of the most exotic problem resolv in my life
	def run_middlewares(self, request):

		str = 'middle = '

		for i in range(len(MIDDLEWARES)):
			str += f'MIDDLEWARES[{i}]('

		for i in range(len(MIDDLEWARES)):
			if i == 0:
				str += 'self.start_response'
			str += ')'

		exec(str)
		exec('middle(request)')


	def __call__(self, environ, start_response):

		request = Request(environ, start_response)
		self.run_middlewares(request)

		try:
			func = self.router.get_route(request.path)

			if func is not None:
				response: Response = func(request)

				return response.make_response()

			else:
				raise InexistentPath('You did not provide a controler function')

		except Exception as e:
			print(e)

		response: Response = PageNotFound(request)

		return response.make_response()
