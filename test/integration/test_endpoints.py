from http import HTTPStatus
from flask.testing import FlaskClient
from pytest import raises ,fixture
from app.main import app


@fixture
def client() -> FlaskClient:
    return app.test_client()


def test_bad_path(client: FlaskClient) -> None:
    response = client.get("/xxxx")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_users_endpoint_returns_200(client: FlaskClient) -> None:
    response = client.get("/users")
    assert response.status_code == HTTPStatus.OK


def test_get_single_user_returns_200(client: FlaskClient) -> None:
    with raises(NotImplementedError):
        response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK


def test_get_single_user_error(client: FlaskClient) -> None:
    user_id_error_provider = 999
    response = client.get(f"/users/{user_id_error_provider}")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_user_returns_202(client: FlaskClient) -> None:
    posted_user = {
        "firstName": "Bartosz",
        "lastName": "Cudny",
        "birthYear": 2009,
        "group": "user"
    }
    response = client.post("/users", json=posted_user)
    assert response.status_code == HTTPStatus.CREATED


def test_create_user_error(client: FlaskClient) -> None:
    posted_user_error = {
        "firstName": 11,
        "lastName": 99,
        "birthYear": "2009",
        "group": "user"
    }
    response = client.post("/users", json=posted_user_error)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_patch_user_returns_200(client: FlaskClient) -> None:
    patched_user = {
        "firstName": "Bartłomiej",
        "lastName": "Jasiński",
        "birthYear": 1985,
        "group": "user"
    }
    user_to_patch_id = 1
    response = client.patch(f"/users/{user_to_patch_id}", json=patched_user)
    assert response.status_code == HTTPStatus.OK


def test_patch_user_error(client: FlaskClient) -> None:
    user_to_patch_id_error_provider = 999
    response = client.patch(f"/users/{user_to_patch_id_error_provider}")
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_user_delete_returns_202(client: FlaskClient) -> None:
    user_to_delete_id = 1
    response = client.delete(f"/users/{user_to_delete_id}")
    assert response.status_code == HTTPStatus.ACCEPTED


def test_user_delete_error(client: FlaskClient) -> None:
    user_id_error_provider = 999
    response = client.delete(f"/users/{user_id_error_provider}")
    assert response.status_code == HTTPStatus.BAD_REQUEST