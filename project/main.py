from models import *

import sys  
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')

from PyHD.response import HttpResponse, Render
from PyHD.router import Path
from PyHD.app import App
from PyHD.register_account_models.auth_process_utils import user_registration

from PyHD.model_managers.models import Query

from wsgiref.simple_server import make_server


app = App()

# Controller file for all functions
# Make a function that takes a request argument, link it to a url and use

# Example controler func
def index(request):

	message = ''

	if request.method == 'POST':

		name = request.POST.get('name')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		user = user_registration(name, password1, password2)

		if type(user) == str:
			message = user
		else:
			message = 'User successfully created'

		context = {
			'user': user,
			'message': message,
			'users': Query.all_objects(AuthUser)
		}

	context = {'message': message, 'user': '', 'users': Query.all_objects(AuthUser)}
	return Render(request, 'index.html', context)


routes = [
	# Here you create new paths

	Path('/', index),
]
    
app.set_routes(routes)

if __name__ == '__main__':
	server = make_server('127.0.0.1', 8000, app)
	server.serve_forever()
