from sqlalchemy import Column

from app.models.BaseModel import BaseModel


class Teacher(BaseModel):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String(255), unique=True, index=True, nullable=False)
