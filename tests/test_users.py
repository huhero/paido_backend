from http import HTTPStatus

from paido_backend.schemas import UserPublic


def test_create_user(client):
    # client = TestClient(app)  # Organizacion

    response = client.post(
        url='/v1/users/',
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

    response = client.post(
        url='/v1/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists.'}

    response = client.post(
        url='/v1/users/',
        json={
            'username': 'testusername1',
            'email': 'test@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'E-mail already exists.'}


def test_read_users(client):
    response = client.get(url='/v1/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == []


def test_read_users_with_data(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        url='/v1/users/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [user_schema]


def test_get_user_by_id(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        url=f'/v1/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema

    response = client.get(url='/v1/users/2')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_get_user_by_id_from_other_user(client, user, token):
    response = client.get(
        url=f'/v1/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions.'}


def test_put_user(client, user, token):
    response = client.put(
        url=f'/v1/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
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


def test_put_wrong_user(client, user, token):
    response = client.put(
        url=f'/v1/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'testusername02',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions.'}


def test_deleted_user(client, user, token):
    response = client.delete(
        url=f'/v1/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User Deleted.'}


def test_deleted_wrong_user(client, user, token):
    response = client.delete(
        url=f'/v1/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions.'}
