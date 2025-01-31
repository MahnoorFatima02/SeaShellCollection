from flask import Blueprint, request, jsonify
from controller.shell_controller import ShellController

shell_bp = Blueprint('shells', __name__)


@shell_bp.route('/shells', methods=['GET'])
async def get_shells():
    return await ShellController.get_shells()


@shell_bp.route('/shells/<int:id>', methods=['GET'])
async def get_shell(id):
    return await ShellController.get_shell(id)

@shell_bp.route('/shells', methods=['POST'])
async def create_shell():
    return await ShellController.create_shell(request.json)

@shell_bp.route('/shells/<int:id>', methods=['PUT'])
async def update_shell(id):
    return await ShellController.update_shell(id, request.json)

@shell_bp.route('/shells/<int:id>', methods=['DELETE'])
async def delete_shell(id):
    return await ShellController.delete_shell(id)