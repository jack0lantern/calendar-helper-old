"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for a list of runserver options.
"""

from flask_script import Manager
import os

from app import create_app

# Setup Flask-Script with command line commands
manager = Manager(create_app)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    print("THIS IS MY PORT NUMBER")
    print(os.environ['PORT'])
    manager.run(port=os.environ['PORT'] if os.environ['PORT'] else 5000)
