from http import HTTPStatus

# import pytest
# from fastapi.testclient import TestClient

# Orgnizar
# exejutar
# afirmar


# @pytest.fixture
# def client():
#     return TestClient(app)


def test_ping(client):
    # client = TestClient(app)  # Organizacion
    response = client.get(url='/ping')  # ejecutar
    assert response.status_code == HTTPStatus.OK  # afirmando
    assert response.json() == {'message': 'pong!'}
