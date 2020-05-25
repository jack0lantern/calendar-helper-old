# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flask import Blueprint, render_template, jsonify, request, Flask
from app.models.gcal import main
# from app.util import logging

import requests
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
    # logging.debug(request.json)
    req_data = request.json
    #
    # {'token': 'lGbfTHXREzcfW0nzAC339k4G', 'team_id': 'TS5PS01B4', 'api_app_id': 'ASJJ4SCLD', 'event': {'client_msg_id': '472abd43-d9b1-4499-bb99-4706a0f3f18b', 'type': 'message', 'text': 'lets say i finish the course what is the next step?', 'user': 'UT6B5SPFU', 'ts': '1590430759.000300', 'team': 'TS5PS01B4', 'blocks': [{'type': 'rich_text', 'block_id': 'njv', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'lets say i finish the course what is the next step?'}]}]}], 'thread_ts': '1589488209.000400', 'parent_user_id': 'UT6B5SPFU', 'channel': 'CS8B30LAV', 'event_ts': '1590430759.000300', 'channel_type': 'channel'}, 'type': 'event_callback', 'event_id': 'Ev014LL0LKFT', 'event_time': 1590430759, 'authed_users': ['USJ3ZP1QC']}
    messageData = {
        'token': req_data['token'],
        'channel': req_data['channel'],
        'text': 'Hi I see your message: ' + req_data['text']
    }
    requests.post('https://slack.com/api/chat.postMessage', messageData)
    return jsonify(request.json)


@main_blueprint.route('/api/button-options', methods = ['POST'])
def process_button_choice():
    return ''


@main_blueprint.route('/api/button', methods = ['POST'])
def send_button_choices():
    return ''