import json

from fastapi import status
from starlette.testclient import TestClient

from app.config.settings import get_settings
from tests.factory import create_user

settings = get_settings()

LIST_USERS_URL = f"{settings.api_prefix_v1}/users/"


def test_list_user(client: TestClient):
    create_user("user1@example.com")
    create_user("user2@example.com")

    response = client.get(LIST_USERS_URL)
    response_json = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) == 2


def test_list_user_skip(client: TestClient):
    create_user("user1@example.com")
    create_user("user2@example.com")

    response = client.get(LIST_USERS_URL, params={"skip": 1})
    response_json = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) == 1


def test_list_user_limit(client: TestClient):
    create_user("user1@example.com")
    create_user("user2@example.com")
    create_user("user3@example.com")
    create_user("user4@example.com")

    response = client.get(LIST_USERS_URL, params={"limit": 2})
    response_json = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json) == 2
