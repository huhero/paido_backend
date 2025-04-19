from jwt import decode

from paido_core.security import ALGORITHM, SECRET_KEY, create_access_token


def test_security_create_access_token():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded['sub'] == data['sub']
    assert 'exp' in decoded
