# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flask import Blueprint, render_template, jsonify, request, Flask
from app.models.gcal import main
from app.util import server_log
# import requests


main_blueprint = Blueprint('main', __name__, template_folder='templates')

# The Home page is accessible to anyone
@main_blueprint.route('/')
def home_page():
    return render_template('main/home_page.html')

# Google verification page
@main_blueprint.route('/getEvents', methods = ['POST'])
def getEvents():
    print("token received! ", request.json)
    # response = requests.get(
    #     url='https://www.googleapis.com/calendar/v3/users/me/settings',
    #     headers={
    #         'Authorization': 'Bearer ' + request.json["token"],
    #     },
    # )
    # response.raise_for_status()
    # print(response.json())
    main()

    return jsonify({"success": request.json["token"]})

@main_blueprint.route('/processmessage', methods = ['POST'])
def process_message():
    server_log.info(request.json)
    return jsonify(request.json)


@main_blueprint.route('/api/button-options', methods = ['POST'])
def process_button_choice():
    return ''


@main_blueprint.route('/api/button', methods = ['POST'])
def send_button_choices():
    return ''