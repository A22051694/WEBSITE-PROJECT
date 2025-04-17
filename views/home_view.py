from flask import Blueprint, render_template

home_view = Blueprint('home', __name__)

@home_view.route('/')
def home():
    return render_template('index.html')
