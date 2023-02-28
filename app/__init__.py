# Import home and dashboard from routes package
from app.routes import home, dashboard
# Use from ... import statement to import the Flask() function
from flask import Flask

# Use def keyword to define a create_app() function
# Indent code blocks by two spaces to contain within function
def create_app(test_config=None):
  # set up app config
#   App should serve any static resources from the root directory and not from the default /static directory
  app = Flask(__name__, static_url_path='/')
#   Trailing slashes are optional
  app.url_map.strict_slashes = False
#   App should use the key when creating server-side sessions
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
#   Decorator turns the function into a route
  @app.route('/hello')
    # Inner function that returns a string
  def hello():
        # Function's return is the route's response
    return 'hello world'
  # Register home blueprint
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  return app