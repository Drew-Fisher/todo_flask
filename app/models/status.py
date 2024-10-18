from sqlalchemy import Column, Integer, String
from app import db

class Status(db.Model):

    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    sequence = Column(Integer, nullable=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Status: {self.name}"
    
    def update(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name