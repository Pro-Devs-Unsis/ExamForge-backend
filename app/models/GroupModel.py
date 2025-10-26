from sqlalchemy import Column, Integer, String

from app.models.BaseModel import BaseModel


class Group(BaseModel):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)