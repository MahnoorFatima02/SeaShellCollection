import os
import sys
import logging
import pytest
from unittest.mock import patch, MagicMock, AsyncMock

# Add the backend directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.shell_model import Shell
from services.shell_service import ShellService

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def async_client(test_client):
    yield test_client

@patch('dao.shell_dao.ShellDAO.create_shell', new_callable=MagicMock)
def test_create_shell(mock_create_shell, async_client, test_app):
    mock_create_shell.return_value = Shell(id=1, name='Shell 1', species='Species 1', description='Description 1', location='Location 1', size='Size 1')
    
    data = {'name': 'Shell 1', 'species': 'Species 1', 'description': 'Description 1', 'location': 'Location 1', 'size': 'Size 1'}

    response = async_client.post('/api/v1/shells', json=data)
    assert response.status_code == 201
    assert response.json['id'] == 1

@patch('dao.shell_dao.ShellDAO.get_all_shells', new_callable=MagicMock)
def test_get_shells(mock_get_all_shells, async_client, test_app):
    mock_get_all_shells.return_value = [
        Shell(id=1, name='Shell 1', species='Species 1', description='Description 1', location='Location 1', size='Size 1'),
        Shell(id=2, name='Shell 2', species='Species 2', description='Description 2', location='Location 2', size='Size 2')
    ]
    
    response = async_client.get('/api/v1/shells')
    assert response.status_code == 200
    assert len(response.json) == 2

@patch('dao.shell_dao.ShellDAO.update_shell', new_callable=MagicMock)
def test_update_shell(mock_update_shell, async_client, test_app):
    mock_update_shell.return_value = Shell(id=1, name='Updated Shell', species='Updated Species', description='Updated Description', location='Updated Location', size='Updated Size')
    
    data = {'name': 'Updated Shell', 'species': 'Updated Species', 'description': 'Updated Description', 'location': 'Updated Location', 'size': 'Updated Size'}

    response = async_client.put('/api/v1/shells/1', json=data)
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Shell'

@patch('services.shell_service.ShellService.delete_shell', new_callable=AsyncMock)
def test_delete_shell(mock_delete_shell, async_client, test_app):
    # Mock the delete operation
    mock_delete_shell.return_value = None
    
    # Perform the delete operation
    delete_response = async_client.delete('/api/v1/shells/1')
    assert delete_response.status_code == 204

@patch('dao.shell_dao.ShellDAO.create_shell', new_callable=MagicMock)
def test_create_shell_without_required_field(mock_create_shell, async_client, test_app):
    mock_create_shell.side_effect = ValueError("species is required")
    
    data = {'name': 'Shell 1', 'species': '', 'description': 'Description 1', 'location': 'Location 1', 'size': 'Size 1'}

    response = async_client.post('/api/v1/shells', json=data)
    assert response.status_code == 400
    assert 'species is required' in response.json.get('error', '')

@patch('dao.shell_dao.ShellDAO.update_shell', new_callable=MagicMock)
def test_update_shell_without_required_field(mock_update_shell, async_client, test_app):
    mock_update_shell.side_effect = ValueError("species is required")
    
    data = {'name': 'Shell 1', 'species': '', 'description': 'Updated Description', 'location': 'Updated Location', 'size': 'Updated Size'}

    response = async_client.put('/api/v1/shells/1', json=data)
    assert response.status_code == 400
    assert 'species is required' in response.json.get('error', '')

def test_invalid_route(async_client, test_app):
    response = async_client.get('/api/v1/invalid_route')
    assert response.status_code == 404
    response_json = response.get_json()
    assert response_json is not None
    assert 'Page not found' in response_json.get('error', '')