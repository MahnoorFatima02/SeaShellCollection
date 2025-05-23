from sqlalchemy import Column, Integer, String, Text
from database.db import Base

class Shell(Base):
    __tablename__ = 'shells'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    species = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(100))
    size = Column(String(50))