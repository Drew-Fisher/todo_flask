from flask import Blueprint, render_template
from app.service import getBoarddefault

board_blueprint = Blueprint('board', __name__)

@board_blueprint.route('/')
def index():
    return render_template('index.html')

@board_blueprint.route('/board')
def board():
    #board_columns = ['To Do', 'In Progress', 'Done']
    #todo_stubs = getStubTodos(1, 100)
    board = getBoarddefault()
    return render_template('board.html', board=board)

@board_blueprint.route('/todo')
def todo(page=None , per_page=None):
    return render_template('todo.html')

@board_blueprint.route('/todo_stubs')
def todo_stubs(page=None , per_page=None):
    return render_template('todo_stub.html')