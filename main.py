"""
------------------------------------------------------------------------
This program is used as the backend for the SlackApp "passVault"
------------------------------------------------------------------------
Author: Karunpreet Dhamnait
Email:  kdhamnai@uoguelph.ca
__updated__ = "2020-12-15"
------------------------------------------------------------------------
"""

import logging
import sqlite3 as sq

from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

from message_block import MessageBlock
from password_util import random_password
from password_util import store_password
from password_util import retrieve_password

logging.basicConfig(level=logging.DEBUG)
app = App()

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# Create a Connection object that represents the database
conn = sq.connect('passwords.db', check_same_thread=False)

# Create a cursor object
cursor = conn.cursor()

# Checks if table (database file) has been created, ignores exception if table exists
try:
    cursor.execute('''CREATE TABLE passwords
                       (platform text, password text, user_id text)''')
    conn.commit()
except sq.OperationalError:
    None

def create_message(user_id: str, channel: str, command, account = "", password = ""):
    # Create a new MessageBlock.
    message_block = MessageBlock(channel)

    # Get the response payload based on user input
    if command == "start":                                                              # Start Menu Message Structure
        message = message_block.get_start_message_payload() 
    elif command == "choice":                                                           # Store Password (Menu) Message Structure
        message = message_block.get_choice_message_payload()
    elif command == "store":                                                            # Store Password Message Structure
        message = message_block.get_store_password_payload(account, password)
    elif command == "get":                                                              # Get Password Message Structure
        message = message_block.get_retrieve_password_payload(account, password)

    return message

# ================ Message Events =============== #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@app.event("message")
def display_message(event, say):
    """Display welcome message after receiving a message that contains "start" """

    # Initialize input message variables
    channel_id = event["channel"]
    user_id = event["user"]
    text = event["text"]
    text_list = list(text.split())

    # slack_bot$ start
    # (Start Menu)
    if len(text_list) < 2 and "start" in text_list:
        message = create_message(user_id,channel_id,"start")
    	
    # slack_bot$ sp
    # (Store Password)
    if len(text_list) < 2 and "sp" in text_list:                                    
    	message = create_message(user_id, channel_id, "choice")

    # slack_bot$ gen_pass <Insert Account Name>
    # (Generate Password)
    if len(text_list) < 4 and "gen_pass" in text_list:
        account = text_list[1]
        password = random_password()
        store_password(conn, account, password, user_id)
        message = create_message(user_id, channel_id, "store", account, password)

    # slack_bot$ create_pass <Insert Account Name> <Insert Password>
    # (Create Password)
    if len(text_list) < 5 and "create_pass" in text_list:
        account = text_list[1]
        password = text_list[2]
        store_password(conn, account, password, user_id)
        message = create_message(user_id, channel_id, "store", account, password)

    # slack_bot$ gp <Insert Account Name>
    # (Get Password)
    if len(text_list) < 4 and "gp" in text_list:
        account = text_list[1]
        password = retrieve_password(conn, account, user_id)
        message = create_message(user_id, channel_id, "get", account, password)

    say(message)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))