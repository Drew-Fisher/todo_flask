from typing import List
from app.models import Todo

def getBoarddefault() -> List[dict]:
    return [
        {
            'status': {
                'name': 'To Do',
            },
            'stubs': [
                {
                    'id': 1,
                    'name': 'Create a new todo',
                    'description': 'Create a new todo with a title and description',
                    'status': 'To Do',
                },
                {
                    'id': 2,
                    'name': 'Update a todo',
                    'description': 'Update a todo with a title and description',
                    'status': 'To Do',
                },
            ]
        },
        {
            'status': {
                'name': 'In Progress',
            },
            'stubs': [
                {
                    'id': 3,
                    'name': 'Delete a todo',
                    'description': 'Delete a todo with a title and description',
                    'status': 'In Progress',
                },
            ]
        },
        {
            'status': {
                'name': 'Done',
            },
            'stubs': [
                {
                    'id': 4,
                    'name': 'List all todos',
                    'description': 'List all todos with a title and description',
                    'status': 'Done',
                },
            ]
        },
    ]

def getBoardStages() -> List[str]:
    return ['To Do', 'In Progress', 'Done']

# todo convert to todo_stub query
def getStubTodos(page: int, limit: int) -> List[Todo]:
    return Todo.query.paginate(page, limit).items