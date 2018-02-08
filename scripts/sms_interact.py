# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from libeary import LiBeary

app = Flask(__name__)
libeary = LiBeary()

@app.route("/sms", methods=['GET', 'POST'])
def sms_process_reply(to_number, BEAR_NUMBER, message_body):
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    text_back = libeary.newMessage(message_body)
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)