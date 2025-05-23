# import pytest
# import pytest_asyncio 
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import asyncio
# from httpx import AsyncClient
# from httpx import ASGITransport
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# from database.db import Base, get_db
# from app import app

# # Use in-memory SQLite for testing
# DATABASE_URL = "sqlite+aiosqlite:///:memory:"


# engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop

# @pytest_asyncio.fixture(scope="session", autouse=True)
# async def prepare_database():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)

# @pytest_asyncio.fixture(scope="function")
# async def async_client(prepare_database):
#     async def override_get_db():
#         async with TestingSessionLocal() as session:
#             yield session
#     app.dependency_overrides[get_db] = override_get_db
    
#     transport = ASGITransport(app=app)
#     async with AsyncClient(transport=transport, base_url="https://test") as ac:
#         yield ac


import pytest
import pytest_asyncio
from testcontainers.mysql import MySqlContainer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import Base, get_db
from app import app
from httpx import AsyncClient, ASGITransport

@pytest.fixture(scope="session")
def mysql_container():
    with MySqlContainer("mysql:8.0") as mysql:
        mysql.start()
        yield mysql

@pytest_asyncio.fixture(scope="session")
async def prepare_database(mysql_container):
    db_url = mysql_container.get_connection_url().replace("mysql://", "mysql+aiomysql://")
    engine = create_async_engine(db_url, echo=True)
    TestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="function")
async def async_client(prepare_database, mysql_container):
    db_url = mysql_container.get_connection_url().replace("mysql://", "mysql+aiomysql://")
    engine = create_async_engine(db_url, echo=True)
    TestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session
    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="https://test") as ac:
        yield ac