# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from datetime import datetime
import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

# TODO: enable csrf for security
USE_CSRF = False
# Instantiate Flask extensions
if USE_CSRF:
    csrf_protect = CSRFProtect()

# Initialize Flask Application
def create_app(extra_config_settings={}):
    """Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    print("THIS IS MY PORT NUMBER")
    print(os.environ['PORT'])
    sys.stdout.flush()
    # Load common settings
    app.config.from_object('app.settings')
    app.config.update(dict(
        SERVER_NAME='0.0.0.0' + os.environ['PORT']
        ))
    # Load environment specific settings
    # app.config.from_object('app.local_settings')

    # Load extra settings from extra_config_settings param
    app.config.update(extra_config_settings)

    if USE_CSRF:
        # Setup WTForms CSRFProtect
        csrf_protect.init_app(app)

    # Register blueprints
    from .views import register_blueprints
    register_blueprints(app)

    # Define bootstrap_is_hidden_field for flask-bootstrap's bootstrap_wtf.html
    from wtforms.fields import HiddenField

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)

    app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter


    @app.context_processor
    def context_processor():
        return dict()

    return app


