import os
import sys
import logging
import pytest
from unittest.mock import patch, AsyncMock

# Add the backend directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SPECIFIC_SHELLS_ENDPOINT = '/api/v1/shells/1'
SHELLS_ENDPOINT =  '/api/v1/shells'
SHELL_NAME = "Shell 1"
SHELL_SPECIES = "Species 1"
SHELL_DESCRIPTION = "Description 1"
SHELL_LOCATION = "Location 1"
SHELL_SIZE = "Size 1"
# nosec: test-only credential
TEST_USERNAME = "testuser"
TEST_PASSWORD = os.environ.get("TEST_PASSWORD", "testpass")


@pytest.fixture
async def auth_headers_fixture(async_client):
    await async_client.post("/api/v1/signup", json={"username": TEST_USERNAME, "password": TEST_PASSWORD})
    response = await async_client.post("/api/v1/login", json={"username": TEST_USERNAME, "password": TEST_PASSWORD})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@patch('dao.shell_dao.ShellDAO.create_shell', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_create_shell(mock_create_shell, async_client, auth_headers_fixture):
    headers = await auth_headers_fixture
    mock_create_shell.return_value = {
        "id": 1,
        "name": SHELL_NAME,
        "species": SHELL_SPECIES,
        "description": SHELL_DESCRIPTION,
        "location": SHELL_LOCATION,
        "size": SHELL_SIZE
    }
    data = {
        'name': SHELL_NAME,
        'species': SHELL_SPECIES,
        'description': SHELL_DESCRIPTION,
        'location': SHELL_LOCATION,
        'size': SHELL_SIZE
        }
    response = await async_client.post(SHELLS_ENDPOINT, json=data, headers=headers)
    assert response.status_code in (200, 201)
    assert response.json()["id"] == 1

@patch('dao.shell_dao.ShellDAO.get_all_shells', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_get_shells(mock_get_all_shells, async_client):
    mock_get_all_shells.return_value = [
        {
            "id": 1,
            "name": "Shell 1",
            "species": "Species 1",
            "description": "Description 1",
            "location": "Location 1",
            "size": "Size 1"
        },
        {
            "id": 2,
            "name": "Shell 2",
            "species": "Species 2",
            "description": "Description 2",
            "location": "Location 2",
            "size": "Size 2"
        }
    ]
    response = await async_client.get(SHELLS_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2

@patch('dao.shell_dao.ShellDAO.update_shell', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_update_shell(mock_update_shell, async_client, auth_headers_fixture):
    headers = await auth_headers_fixture
    mock_update_shell.return_value = {
        "id": 1,
        "name": "Updated Shell",
        "species": "Updated Species",
        "description": "Updated Description",
        "location": "Updated Location",
        "size": "Updated Size"
    }
    data = {'name': 'Updated Shell', 'species': 'Updated Species', 'description': 'Updated Description', 'location': 'Updated Location', 'size': 'Updated Size'}
    response = await async_client.put(SPECIFIC_SHELLS_ENDPOINT, json=data, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == 'Updated Shell'

@patch('services.shell_service.ShellService.delete_shell', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_delete_shell(mock_delete_shell, async_client, auth_headers_fixture):
    headers = await auth_headers_fixture
    mock_delete_shell.return_value = None
    delete_response = await async_client.delete(SPECIFIC_SHELLS_ENDPOINT, headers=headers)
    assert delete_response.status_code == 204

@patch('dao.shell_dao.ShellDAO.create_shell', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_create_shell_without_required_field(mock_create_shell, async_client, auth_headers_fixture):
    headers = await auth_headers_fixture
    mock_create_shell.return_value = {
        "id": 1,
        "name": SHELL_NAME,
        "species": SHELL_SPECIES,
        "description": SHELL_DESCRIPTION,
        "location": SHELL_LOCATION,
        "size": SHELL_SIZE
    }
    data = {'name': 'Shell 1', 'species': '', 'description': 'Description 1', 'location': 'Location 1', 'size': 'Size 1'}
    response = await async_client.post(SHELLS_ENDPOINT, json=data, headers=headers)
    assert response.status_code == 422
    # Accept either 'error' or 'detail' key for error message
    error_msg = response.json().get('detail', '')
    assert error_msg

@patch('dao.shell_dao.ShellDAO.update_shell', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_update_shell_without_required_field(mock_update_shell, async_client, auth_headers_fixture):
    headers = await auth_headers_fixture
    mock_update_shell.return_value = {
        "id": 1,
        "name": "Updated Shell",
        "species": "Updated Species",
        "description": "Updated Description",
        "location": "Updated Location",
        "size": "Updated Size"
    }
    data = {'name': 'Shell 1', 'species': '', 'description': 'Updated Description', 'location': 'Updated Location', 'size': 'Updated Size'}
    response = await async_client.put(SPECIFIC_SHELLS_ENDPOINT, json=data, headers=headers)
    assert response.status_code == 422
    error_msg = response.json().get('detail', '')
    assert error_msg

@pytest.mark.asyncio
async def test_invalid_route(async_client):
    response = await async_client.get('/api/v1/invalid_route')
    assert response.status_code == 404
    response_json = response.json()
    # Accept either 'error' or 'detail' key for error message
    error_msg = response_json.get('error', '') or response_json.get('detail', '')
    assert error_msg  # Just check that some error message is present