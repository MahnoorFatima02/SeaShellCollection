from model.user_model import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class UserDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_username(self, username: str):
        result = await self.db.execute(select(User).where(User.username == username))
        return result.scalars().first()

    async def create_user(self, username: str, hashed_password: str):
        user = User(username=username, hashed_password=hashed_password)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user