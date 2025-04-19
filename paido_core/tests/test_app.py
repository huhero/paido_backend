from http import HTTPStatus

from paido_core.schemas import UserPublic


def test_root_debe_retornar_hola_mundo(client):
    # client = TestClient(app)  # Organizar

    response = client.get('/')  # actuar

    assert response.status_code == HTTPStatus.OK  # afirmar
    assert response.json() == {'message': 'hola mundo!'}  # afirmar


def test_app_create_user(client):
    response = client.post(
        url='/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_app_create_user_already_exists(client, user):
    response = client.post(
        url='/users/',
        json={
            'username': user.username,
            'email': user.email,
            'password': user.password,
        },
    )
    assert response.status_code != HTTPStatus.OK
    # assert response.json() == {'message': 'User already registered'}


def test_app_read_users(client):
    response = client.get(url='/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_app_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(url='/users/')
    assert response.json() == {'users': [user_schema]}


def test_app_read_user_by_id(client, user):
    response = client.get(url=f'/users/{user.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Teste',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_app_read_user_by_id_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_app_update_user(client, user, token):
    response = client.put(
        url=f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_app_update_user_not_found(client, user, token):
    response = client.put(
        url=f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'hola',
            'email': 'hola@example.com',
            'password': 'hola',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_app_update_user_wrong_token(client, user):
    response = client.put(
        url=f'/users/{user.id}',
        headers={'Authorization': 'Bearer TOKEN_ERRADO'},
        json={
            'username': 'hola',
            'email': 'hola@example.com',
            'password': 'hola',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_app_delete_user(client, user, token):
    response = client.delete(
        url=f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_app_delete_user_not_found(client, user, token):
    response = client.delete(
        url=f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_app_delete_user_wrong_token(client, user):
    response = client.delete(
        url=f'/users/{user.id}',
        headers={'Authorization': 'Bearer TOKEN_ERRADO'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_app_get_token(client, user):
    response = client.post(
        url='/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_app_get_token_with_error_password(client, user):
    response = client.post(
        url='/token',
        data={'username': user.email, 'password': 'other password'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
