from sqlalchemy import Column, String, Integer

from app.models.BaseModel import BaseModel


class Classroom(BaseModel):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    type = Column(String(255), nullable=False)