from pytest import raises
from pytest import fixture
from unittest.mock import Mock, call

from app.controllers import UserService
from app.repository import UserRepository


@fixture
def repository() -> Mock:
    return Mock(UserRepository)


@fixture
def controller(repository: Mock) -> UserService:
    return UserService(repository=repository)


def test_user_service_return_on_get_method(controller: UserService) -> None:
    assert controller.get_all_users() is not None


def test_call_repository_on_get_method(
        controller: UserService,
        repository: Mock
) -> None:
    controller.get_all_users()
    expected = call()
    assert expected in repository.get.mock_calls
