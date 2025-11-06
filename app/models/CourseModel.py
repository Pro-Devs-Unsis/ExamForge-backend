from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.BaseModel import BaseModel


class Course(BaseModel):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    semester = Column(String(255), nullable=False)
    academicYear = Column(String(255), nullable=False)

    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete="CASCADE"), unique=True, nullable=False)
