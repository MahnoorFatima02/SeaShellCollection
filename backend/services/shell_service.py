from dao.shell_dao import ShellDAO

class ShellService:
    def __init__(self, dao: ShellDAO):
        self.dao = dao

    async def get_all_shells(self):
        return await self.dao.get_all_shells()

    async def create_shell(self, data):
        return await self.dao.create_shell(data)

    async def get_shell(self, id):
        return await self.dao.get_shell(id)

    async def update_shell(self, id, data):
        return await self.dao.update_shell(id, data)

    async def delete_shell(self, id):
        return await self.dao.delete_shell(id)
    
    async def get_user_name(self):
        return await self.dao.get_user_name()