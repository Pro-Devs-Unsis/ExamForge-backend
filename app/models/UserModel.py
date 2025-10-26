from sqlalchemy import Column, Integer, String

from app.models.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    passwordHash = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)