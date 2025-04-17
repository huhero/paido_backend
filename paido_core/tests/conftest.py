import pytest
from fastapi.testclient import TestClient

from paido_core.app import app


@pytest.fixture
def client():
    return TestClient(app)
