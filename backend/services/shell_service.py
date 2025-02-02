from dao.shell_dao import ShellDAO

class ShellService:
    def __init__(self, dao: ShellDAO):
        self.dao = dao

    async def get_all_shells(self):
        return self.dao.get_all_shells()

    async def create_shell(self, data):
        return self.dao.create_shell(data)

    async def get_shell(self, id):
        self.dao.get_shell(id)

    async def update_shell(self, id, data):
        print(f"Updating shell with ID: {id}")
        shell = self.dao.update_shell(id, data)
        return shell

    async def delete_shell(self, id):
        self.dao.get_shell(id)
        self.dao.delete_shell(id)