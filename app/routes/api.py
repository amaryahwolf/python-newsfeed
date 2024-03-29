from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

# POST route to signup, create new user and initialize session
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()
  
  try:
  # create a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )
    # save in database
    db.add(newUser)
    db.commit()
    print('success!')
  except:
    print(sys.exe_info()[0])
    # Deployment safeguard
    db.rollback()
    return jsonify(message = 'Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)

# POST route to logout
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

# POST route to login
@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Incorrect credentials'), 400

  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400

  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)