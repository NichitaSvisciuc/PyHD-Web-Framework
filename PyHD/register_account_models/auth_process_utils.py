import sys
sys.path.append('C:/projects/PyHDproject/PyHD-Web-Framework')
from PyHD.model_managers.models import Query
from project.models import AuthUser
from PyHD.register_account_models.auth_models import User

from datetime import date


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
