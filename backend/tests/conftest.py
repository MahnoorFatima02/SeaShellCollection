import os
import sys
import pytest
from flask import Flask
from unittest.mock import MagicMock

# Add the backend directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import Config


@pytest.fixture(scope='session')
def test_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        # Register blueprints
        from routes.shell_routes import shell_bp
        app.register_blueprint(shell_bp, url_prefix='/api/v1')
        
        # Register error handlers
        from app import register_error_handlers
        register_error_handlers(app)
        
        yield app
       
@pytest.fixture(scope='function')
def test_client(test_app):
    client = test_app.test_client()
    client.environ_base["werkzeug.debug"] = True
    return client

@pytest.fixture(scope='function')
def mock_db():
    mock_db = MagicMock()
    yield mock_db