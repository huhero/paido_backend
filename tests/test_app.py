from http import HTTPStatus

# import pytest
# from fastapi.testclient import TestClient

# Orgnizar
# exejutar
# afirmar


# @pytest.fixture
# def client():
#     return TestClient(app)


def test_read_root_retornar_ok_hola_munda(client):
    # client = TestClient(app)  # Organizacion
    response = client.get('/')  # ejecutar
    assert response.status_code == HTTPStatus.OK  # afirmando
    assert response.json() == {'message': 'Hola Mundo!'}


def test_create_user(client):
    # client = TestClient(app)  # Organizacion

    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {'username': 'testusername', 'email': 'test@test.com', 'id': 1}
    ]


def test_get_user_by_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }

    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_put_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername02',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername02',
        'email': 'test@test.com',
        'id': 1,
    }

    response = client.put(
        '/users/2',
        json={
            'username': 'testusername02',
            'email': 'test@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_deleted_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User Deleted.'}

    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
