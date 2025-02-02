from flask import jsonify
from utils.custom_exceptions import NotFoundException, ValidationException, InternalServerException

def register_error_handlers(app):
    @app.errorhandler(ValidationException)
    def handle_validation_error(error):
        print("Handling VALIDATION validation error")
        return jsonify({"error": str(error)}), 400

    @app.errorhandler(InternalServerException)
    def handle_internal_server_error(error):
        return jsonify({"error": str(error)}), 500

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        return jsonify({"error": "An unexpected error occurred"}), 500
    
    @app.errorhandler(404)
    @app.errorhandler(NotFoundException)
    def handle_not_found_error(error):
        return jsonify({"error": "Resource Not found"}), 404
    