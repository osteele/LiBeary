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


@app.route("/sms", methods=['GET', 'POST'])
def inbound_sms():
    body = request.values.get('Body', None)

    resp = MessagingResponse()
    if "request" in body.lower():
        resp.message('Thanks for requesting a book! If it isn\'t already on its way, I\'ll request it immediately.')
    elif "recommend" in body.lower():
        book_rec = "Moby Dick"
        resp.message('I recommend %s' % (book_rec))
    else:
        resp.message('Sorry, say that again?')

    print(body) #prints out the message body!!!

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)