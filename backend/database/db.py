from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.config import Config
import ssl


DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

# Create SSL context for Neon/Postgres
ssl_context = ssl.create_default_context()


# Create the async engine with SSL
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}
)

# Create a session factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency for getting the database session
async def get_db():
    async with async_session() as session:
        yield session