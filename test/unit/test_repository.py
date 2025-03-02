from app.repository import UserRepository


def test_user_repository_return_on_get_method() -> None:
    assert UserRepository is not None


def test_user_repository_raises_on_get_method() -> None:
    repository = UserRepository()
