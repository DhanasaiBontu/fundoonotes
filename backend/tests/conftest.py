import pytest
from fastapi.testclient import TestClient
from src.app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def test_user():
    return {
        "email": "pytest_user@example.com",
        "password": "pytest123"
    }
