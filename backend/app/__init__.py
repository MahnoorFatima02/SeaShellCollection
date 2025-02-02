
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config.config import Config
from flask_swagger_ui import get_swaggerui_blueprint
from swagger.swagger import template
from flask_migrate import Migrate, upgrade
from .error_handlers import register_error_handlers 

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
 
    # Create database tables
    with app.app_context():
        upgrade()
    
    # Register blueprints
    from routes.shell_routes import shell_bp 
    app.register_blueprint(shell_bp, url_prefix='/api/v1')


    # Serve swagger.json
    @app.route('/static/swagger.json')
    def serve_swagger():
        return jsonify(template)

    # Swagger UI configuration
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "SeaShell API"
        }
    )
    
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
    
    # Register custom error handlers
    register_error_handlers(app)
    
    
    return app
