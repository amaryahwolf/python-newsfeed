from flask import Blueprint, render_template

# Prefix every route in blueprint with /dashboard
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')