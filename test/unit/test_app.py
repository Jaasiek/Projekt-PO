from flask import Flask

from app.main import app
from app.main import get_users, get_single_user, create_user, patch_user, delete_user


def test_app_is_flask_instance() -> None:
    assert isinstance(app, Flask)