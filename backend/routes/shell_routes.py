from flask import Blueprint, request, jsonify
from controller.shell_controller import ShellController

# Create an instance of ShellController
shell_controller = ShellController()

shell_bp = Blueprint('shells', __name__)

@shell_bp.route('/shells', methods=['GET'])
async def get_shells():
    return await shell_controller.get_shells()

@shell_bp.route('/shells/<int:id>', methods=['GET'])
async def get_shell(id):
    return await shell_controller.get_shell(id)

@shell_bp.route('/shells', methods=['POST'])
async def create_shell():
    return await shell_controller.create_shell()

@shell_bp.route('/shells/<int:id>', methods=['PUT'])
async def update_shell(id):
    return await shell_controller.update_shell(id)

@shell_bp.route('/shells/<int:id>', methods=['DELETE'])
async def delete_shell(id):
    return await shell_controller.delete_shell(id)