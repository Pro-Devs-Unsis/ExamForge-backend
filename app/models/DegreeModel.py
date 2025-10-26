from sqlalchemy import Column, String, Integer

from app.models.BaseModel import BaseModel


class Degree(BaseModel):
    __tablename__ = 'degrees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)