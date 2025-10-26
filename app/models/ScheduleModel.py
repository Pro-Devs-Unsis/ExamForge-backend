from sqlalchemy import Column, String, Integer

from app.models.BaseModel import BaseModel


class Schedule(BaseModel):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, index=True)
    dayOfWeek = Column(String(2), nullable=False)
    startTime = Column(String(255), nullable=False)
    endTime = Column(String(255), nullable=False)