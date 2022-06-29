import json
import sys
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')  


from jinja2 import Environment, FileSystemLoader

from PyHD.request import Request

from settings import TEMPLATES


file_content_types = {
	'html': 'text/html',
	'htm':  'text/html',
	'css':  'text/css',
	'js':   'text/javascript',
	'mkv':  'video/mkv',
}

class Response:

	"""
	Base Response Class
	"""
	__slots__ = ('headers', 'status_code', 'start_response', 'content_type', 'response_content')

	def __init__(self, request: Request, status_code: str, content_type: str):
		self.headers = []
		self.status_code = status_code
		self.start_response = request.start_response
		self.content_type = content_type
		self.response_content = []
		
	def make_response(self):

		self.start_response(self.status_code, [('Content-Type', self.content_type)])

		return self.response_content   


class HttpResponse(Response):

	"""
	Return pure http response when given a text as content
	"""

	def __init__(self, request: Request, content, status_code='200 OK', content_type='text/html'):

		super().__init__(request, status_code, content_type)
		if type(content) == str:
			content = content.encode()
		self.response_content.append(content)


class Render(Response):

	""" Loads a html template and aplly jinja on it """

	def __init__(self, request: Request, filename: str, context=None, status_code='200 OK', content_type='text/html'):

		super().__init__(request, status_code, content_type)
		
		file_loader = FileSystemLoader(TEMPLATES)
		env = Environment(loader=file_loader)
		template = env.get_template(filename)
		output = template.render(context)

		self.response_content.append(output.encode())


class JsonResponse(Response):

	""" Retorns a json response """

	def __init__(self, request: Request, json_response_body, status_code='200 OK', content_type='application/json'):

		super().__init__(request, status_code, content_type)

		if str(json_response_body) == str:
			self.response_content.append(json.loads(json_response_body))


class ErrorResponse(Response):
	def __init__(self, request: Request, error_code: str):
		super().__init__(request, '404 Not Found', 'text/html')
		self.response_content.append("404 Not Found".encode())


class PageNotFound(ErrorResponse):
	def __init__(self, request):
		super().__init__(request, '404 Not Found')