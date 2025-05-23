from passlib.context import CryptContext
from dao.user_dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    async def create_user(self, username: str, password: str):
        hashed_password = pwd_context.hash(password)
        return await self.dao.create_user(username, hashed_password)

    async def get_user(self, username: str):
        return await self.dao.get_by_username(username)