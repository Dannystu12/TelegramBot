#!flask/bin/python
from flask import Flask
from flask import request
import json
import re
import utils

app = Flask(__name__)

@app.route('/<token>', methods=['POST'])
def recieve_new_messages(token):
    #Check that request is a post request and that the token is valid
    if request.method == 'POST' and token == utils.get_token():
        try:
            # Parse the response
            update_data = json.loads(request.data)
            for update in update_data["result"]:
                try:
                    message = update.get('message', {})
                    message_text = message.get('text','')
                    if utils.should_forward(message_text):
                        chat_id = message.get('chat', {}).get('id', '')
                        message_id =  message.get('message_id', '')
                        print "MESSAGE_ID: " + str(message_id)
                        print "CHAT_ID: " + str(chat_id)
                        if len(str(chat_id)) == 0 or len(str(message_id)) == 0:
                            print("Could not retrieve chat or message id")
                        utils.forward_message(chat_id, message_id)

                except Exception as e:
                    print e
                    continue
        except Exception as e:
            print e
    return ''

if __name__ == '__main__':
    app.run(debug=True)
