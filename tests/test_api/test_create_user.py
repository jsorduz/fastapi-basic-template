import json

from fastapi import status
from starlette.testclient import TestClient

from app.config.settings import get_settings
from tests.factory import create_user

settings = get_settings()

CREATE_USER_URL = f"{settings.api_prefix_v1}/users/"


def test_create_user(client: TestClient):
    data = {"email": "user@example.com", "password": "s3cret"}

    response = client.post(CREATE_USER_URL, json=data)
    response_json = json.loads(response.content)

    assert response.status_code == status.HTTP_201_CREATED
    assert response_json["email"] == data["email"]
    for expected_key in ("id", "created_at", "modified_at"):
        assert expected_key in response_json.keys()


def test_create_existing_user(client: TestClient):
    email = "user@example.com"
    data = {"email": email, "password": "s3cret"}
    create_user(email)

    response = client.post(CREATE_USER_URL, json=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
