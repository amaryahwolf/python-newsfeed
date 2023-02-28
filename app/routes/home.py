# Module that belongs to the routes package
# Import Blueprint() (lets us consolidate routes onto a single bp object that the parent app can register later) and render_template() (responds with a template instead of a string) functions from Flask module
from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')