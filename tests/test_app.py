from http import HTTPStatus

from fastapi.testclient import TestClient

from paido_backend.app import app

# Orgnizar
# exejutar
# afirmar


def test_read_root_retornar_ok_hola_munda():
    client = TestClient(app)  # Organizacion
    response = client.get("/")  # ejecutar
    assert response.status_code == HTTPStatus.OK  # afirmando
    assert response.json() == {"message": "Hola Mundo!"}
