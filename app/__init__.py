# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from datetime import datetime
import sys
import os

from flask import Flask


# Initialize Flask Application
def create_app(extra_config_settings={}):
    """Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    port = os.getenv('PORT', 5000)
    os.environ['FLASK_RUN_PORT'] = str(port)
    sys.stdout.flush()

    # Load extra settings from extra_config_settings param
    app.config.update(extra_config_settings)

    # Register blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    return app
