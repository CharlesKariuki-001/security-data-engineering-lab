
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_valid_transaction():
    response = client.post(
        "/transactions",
        json={"amount": 500}
    )

    assert response.status_code == 200
    assert response.json()["amount"] == 500.0
    assert response.json()["status"] == "accepted"


def test_negative_transaction():
    response = client.post(
        "/transactions",
        json={"amount": -500}
    )

    assert response.status_code == 422


def test_missing_amount():
    response = client.post(
        "/transactions",
        json={}
    )

    assert response.status_code == 422
