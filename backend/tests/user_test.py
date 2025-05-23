import pytest
import os

SIGNUP_SHELLS_ENDPOINT = '/api/v1/signup'
LOGIN_SHELLS_ENDPOINT =  '/api/v1/login'
SHELL_NAME = "Shell 1"
SHELL_SPECIES = "Species 1"
SHELL_DESCRIPTION = "Description 1"
SHELL_LOCATION = "Location 1"
SHELL_SIZE = "Size 1"
# nosec: test-only credential
TEST_USERNAME = "testuser22"
TEST_PASSWORD = os.environ.get("TEST_PASSWORD", "testpass")

@pytest.mark.asyncio
async def test_user_registration_and_login(async_client):
    # Register user
    response = await async_client.post(SIGNUP_SHELLS_ENDPOINT, json={"username": TEST_USERNAME, "password": TEST_PASSWORD})
    assert response.status_code == 200
    assert response.json()["msg"] == "User created"

    # Login user
    response = await async_client.post(LOGIN_SHELLS_ENDPOINT, json={"username": TEST_USERNAME, "password": TEST_PASSWORD})
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token

    # Use token for protected endpoint
    headers = {"Authorization": f"Bearer {token}"}
    shell_data = {
        "name": SHELL_NAME,
        "species": SHELL_SPECIES,
        "description": SHELL_DESCRIPTION,
        "location": SHELL_LOCATION,
        "size": SHELL_SIZE
    }
    create_response = await async_client.post("/api/v1/shells", json=shell_data, headers=headers)
    assert create_response.status_code in (200, 201)
    assert create_response.json()["name"] == "Shell 1"