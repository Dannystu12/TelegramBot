import re
import requests

TOKEN = "797024081:AAGsxyOl9rIHf-mwny0Rm9UQJaljvTaFcI0"
SHOULD_FORWARD_REGEXP = re.compile(r'(RESISTANCE)')
BASE_URL = "https://api.telegram.org/bot%s" % TOKEN
FORWARD_MESSAGE_ENDPOINT = "/forwardMessage"
CHAT_ID_FORWARD = "-294276091"

def get_token():
    '''Token for api endpoint'''
    return TOKEN

def should_forward(message):
    '''Check if message contains RESISTANCE string'''
    if SHOULD_FORWARD_REGEXP.search(message):
        return True
    else:
        return False

def forward_message(from_chat_id, message_id):
    '''Takes a message object and forwards it to specified chat'''
    data = {
        "chat_id": CHAT_ID_FORWARD,
        "from_chat_id": from_chat_id,
        "message_id": message_id
    }
    result = requests.post(BASE_URL + FORWARD_MESSAGE_ENDPOINT, json=data)
