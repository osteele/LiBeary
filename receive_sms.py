"""
Receives SMS messages, parses and responds to them based on what they include
"""

# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from libeary import LiBeary
# import send_sms

app = Flask(__name__)
libeary = LiBeary()

SLACK_PHONE_NUMBER = os.getenv('SLACK_PHONE_NUMBER')

@app.route("/sms", methods=['GET', 'POST'])
def inbound_sms():
    body = request.values.get('Body', None)

    resp = MessagingResponse()
    if "request" in body.lower():
        request_body = (body.lower().replace("request ", ""))
        request_body = request_body.replace(" ", "_")
        # print(request_body)
        os.system("python send_sms.py %s %s" % (SLACK_PHONE_NUMBER, request_body))
        resp.message('Thanks for requesting a book! Your request has been submitted.')
    elif "recommend" in body.lower():
        book_rec = libeary.makeRecommendation(body)
        resp.message('I recommend %s' % (book_rec))
    else:
        resp.message('Sorry, say that again?')

    # print(body) #prints out the message body!!!

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)