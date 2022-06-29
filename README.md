# PyHD-Web-Framework
 My experimental web framework

packages to install:
- pip install peewee
- pip install jinja2

If you are familiar with django framework u will see here a lot of things from it

1. To create models go to project file and write the models code
2. Run in the same directory in console - python migrate.py 
3. In the same directory u will see main.py file, this is response controller or views as they're called in django write ur bussiness logic in them
4. In PyHD/response.py u can check all aviable response functions below the main Response class
5. In main directory a settings.py file is located, same as in django there are stored all core variables
6. Account create function and User interface model are provided
7. Jinja template language is provided, parse your context variable as third argument after 'template_file_name' and 'request'
8. Database ORM calls are provided : Query.all_objects(__model_name__)
9. WSGI server is set up already
10. To access post data from a form just call 'request.POST.get['__name_of_input__']'
11. Link router is implemented below the controllers, made like routes = [Path('__your_url__/', __view_func__), ...]
