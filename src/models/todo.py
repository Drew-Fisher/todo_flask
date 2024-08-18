class Todo:
    def __init__(self, id, title, description, state):
        self.id = id
        self.title = title
        self.description = description
        self.stae = state

    def __str__(self):
        return f"Todo: {self.id} {self.title} {self.description} {self.done}"
    
    def update(self, title, description, state):
        if self.state == 'done' or self.state == 'cancelled':
            raise Exception("Cannot update a todo that is done or cancelled")
        self.title = title
        self.description = description
    
    def set_state(self, state):
        self.state = state