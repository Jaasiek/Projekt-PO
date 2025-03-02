from flask import Flask, request

from app.main import app
from app.main import get_users, get_single_user, create_user, patch_user, delete_user


def test_app_is_flask_instance() -> None:
    assert isinstance(app, Flask)


def test_get_users_exists() -> None:
    get_users()


def test_get_single_user_exists() -> None:
    user_id = 1
    get_single_user(id=user_id)


def test_create_user_exists() -> None:
    request.data = {
        "firstName": "Bartosz",
        "lastName": "Cudny",
        "birthYear": 2009,
        "group": "user"
    }
    create_user()


def test_patch_user_exists() -> None:
    user_id = 1
    request.data = {
        "firstName": "Krzysztof",
    }
    patch_user(id=user_id)


def test_delete_user_exists() -> None:
    user_id = 1
    delete_user(id=user_id)
