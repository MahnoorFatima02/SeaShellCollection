from flask import Blueprint, request, jsonify
from services.shell_service import ShellService


class ShellController:
    @staticmethod
    async def get_shells():
        shells = await ShellService.get_all_shells()
        return jsonify([shell.to_dict() for shell in shells])

    @staticmethod
    async def get_shell(id):
        shell = await ShellService.get_shell(id)
        return jsonify(shell.to_dict() if shell else {})

    @staticmethod
    async def create_shell(data):
        shell = await ShellService.create_shell(data)
        return jsonify(shell.to_dict()), 201


    @staticmethod
    async def update_shell(id, data):
        shell = await ShellService.update_shell(id, data)
        return jsonify(shell.to_dict() if shell else {})

    @staticmethod
    async def delete_shell(id):
        await ShellService.delete_shell(id)
        return '', 204