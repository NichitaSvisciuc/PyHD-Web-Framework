import sys, os
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')
from PyHD.model_managers.models import Query
from PyHD.register_account_models.auth_models import User

try:
    from project.models import AuthUser
except Exception as e:
    pass

from datetime import date

import random
import string
import requests


def create_user(
    username: str,
    password: str,
    email='',
    first_name='',
    last_name='',
    is_active=True,
    is_authenticated=False,
    is_staff=False,
) -> None:
    """ Creates a user instance with given credentials """
    safe_password = User.make_password(password)

    try:
        user = AuthUser.create(
            username=username,
            password=safe_password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_authenticated=is_authenticated,
            is_active=is_active,
            date_created=date.today()
        )
        user.save()
    except ValueError as e:
        print('Create a user table or make your migrations')


def user_registration(
    username: str,
    password1: str,
    password2: str,
    email='',
    first_name='',
    last_name='',
    is_active=True,
    is_authenticated=False,
) -> str:
    """ Checks the validity of given credentials """
    usernames = [user.username for user in Query.all_objects(AuthUser)]
    if username in usernames:
        return 'Such username already exists, it must be unique'
    elif password1 != password2:
        return 'Passwords didnt match'
    else:
        create_user(username,
                    password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=is_active,
                    is_authenticated=is_authenticated,
                    is_staff=False,
                    )
        return 'Created'


def authenticate(username: str, password: str):
    """ Returns a user instance if credentials are valid and it exists """
    try:
        users = Query.all_objects(AuthUser)

        for user in users:
            if user.username == username:
                safe_password = User.make_password(password)
                if safe_password == user.password:
                    return user
                else:
                    return None
            else:
                return None
    except ModuleNotFoundError:
        print('Auth user model not implemented')


def login(user, request=None):
    """ Creates a session id and saves it to browser cookies """

    if user is not None:

        letters = string.ascii_letters
        session_id = ''.join(random.choice(letters) for i in range(20))
        print('session_id', session_id)

        cookies = {'session_token': session_id}
        r = requests.post('https://google.com', cookies=cookies)

        s = requests.session()
        cookie_obj = requests.cookies.create_cookie(domain="google.com", name="session_token", value=session_id)
        s.cookies.set_cookie(cookie_obj)
