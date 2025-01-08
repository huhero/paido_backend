import pytest
from fastapi.testclient import TestClient

from paido_backend.app import app

# Orgnizar
# exejutar
# afirmar


@pytest.fixture
def client():
    return TestClient(app)
