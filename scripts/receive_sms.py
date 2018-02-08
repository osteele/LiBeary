"""
Receives SMS messages sent to our Twilio phone number
Parses and responds to them based on what they include
Modified from the Twilio QuickStart
"""

# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
import os
import subprocess
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
        #remove the word "request" in whatever form, as well as quotes around the title
        request_body = body.replace("request ", "")
        request_body = request_body.replace("Request ", "")
        request_body = request_body.replace("REQUEST ", "")
        request_body = request_body.replace("\"", "")
        #call the script send_sms.py
        subprocess.call(["python", "send_sms.py", SLACK_PHONE_NUMBER, request_body])
        resp.message('Thanks for requesting a book! Your request has been submitted.')
    elif "recommend" in body.lower():
        book_rec = libeary.makeRecommendation(body)
        resp.message('I recommend %s' % (book_rec))
    else:
        resp.message('Sorry, say that again?')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)