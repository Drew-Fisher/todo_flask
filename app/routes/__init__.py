from flask import Blueprint, render_template
from .board import board_blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')