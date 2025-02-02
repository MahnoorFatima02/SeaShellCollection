from flask import Blueprint, request, jsonify
from services.shell_service import ShellService
from utils.validation import validate_shell_data
from utils.response import create_response
from dao.shell_dao import ShellDAO

class ShellController:
    def __init__(self):
        self.dao = ShellDAO()
        self.service = ShellService(self.dao)
    
    async def get_shells(self):
        shells = await self.service.get_all_shells()
        return jsonify([shell.to_dict() for shell in shells])

    async def get_shell(self, id):
        shell = await self.service.get_shell(id)
        return create_response(shell)

    async def create_shell(self):
        data = request.get_json()
        validate_shell_data(data)
        shell = await self.service.create_shell(data)
        return create_response(shell, 201)


    async def update_shell(self, id):
        data = request.get_json()
        validate_shell_data(data)
        shell = await self.service.update_shell(id, data)
        return create_response(shell)

    async def delete_shell(self,id):
        await  self.service.delete_shell(id)
        return create_response(status_code=204)