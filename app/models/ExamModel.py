from sqlalchemy import Column, String, Integer

from app.models.BaseModel import BaseModel


class Exam(BaseModel):
    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(255), nullable=False)
    startTime = Column(String(255), nullable=False)
    endTime = Column(String(255), nullable=False)