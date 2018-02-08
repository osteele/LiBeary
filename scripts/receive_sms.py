"""
Receives SMS messages
"""

# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client

app = Flask(__name__)

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/sms", methods=['GET', 'POST'])
def inbound_sms():
    body = request.values.get('Body', None)

    resp = MessagingResponse()
    print(body) #prints out the message body!!!

    return str(resp)
    

# @app.route('/')
# def hello_world():
#     return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)