from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from model.shell_model import Shell

class ShellDAO:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_all_shells(self):
        result = await self.db_session.execute(select(Shell))
        return result.scalars().all()

    async def create_shell(self, data: dict):
        shell = Shell(**data)
        self.db_session.add(shell)
        await self.db_session.commit()
        await self.db_session.refresh(shell)
        return shell

    async def get_shell(self, id: int):
        result = await self.db_session.execute(select(Shell).where(Shell.id == id))
        shell = result.scalars().first()
        if not shell:
            raise ValueError("Shell not found")
        return shell

    async def update_shell(self, id: int, data: dict):
        shell = await self.get_shell(id)
        for key, value in data.items():
            setattr(shell, key, value)
        await self.db_session.commit()
        return shell

    async def delete_shell(self, id: int):
        shell = await self.get_shell(id)
        await self.db_session.delete(shell)
        await self.db_session.commit()