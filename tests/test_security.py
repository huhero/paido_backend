from http import HTTPStatus

from jwt import decode

from paido_core.security import create_access_token, settings


def test_jwt():
    data = {'sub': 'test@test.com'}

    token = create_access_token(data)

    result = decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    assert result['sub'] == data['sub']
    assert result['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        url='/v1/users/1',
        headers={'Authorization': 'Bearer Token_invalidado'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
