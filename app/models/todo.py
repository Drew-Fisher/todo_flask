from sqlalchemy import Column, Integer, String
from app import db

class Todo(db.Model):

    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    state = Column(String, nullable=False)


    def __init__(self, id, title, description, state):
        self.id = id
        self.title = title
        self.description = description
        self.state = state

    def __str__(self):
        return f"Todo: {self.id} {self.title} {self.description} {self.done}"
    
    def update(self, title, description, state):
        if self.state == 'done' or self.state == 'cancelled':
            raise Exception("Cannot update a todo that is done or cancelled")
        self.title = title
        self.description = description
    
    def set_state(self, state):
        self.state = state