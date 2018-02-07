"""
Practice getting messages sent via the Twilio REST API (from the Twilio QuickStart)
"""

import re
import os

import click
from twilio.rest import Client

account_sid = "AC7f89127ce345d9cac1ee5139e0357ba8"
auth_token = "6430dedf84a61639d01e54e5c868fb80"
from_number = "+16173963238"

PHONE_NUMBER_RE = re.compile(r'^\+1\d{10}$')
PHONE_NUMBER_EXAMPLE = '+161723351010'

@click.command()
# When running this from terminal, follow run command with these arguments
@click.argument('to_number')
@click.argument('message_body', default='hello')

def send_sms_message(to_number, message_body):
    assert PHONE_NUMBER_RE.match(to_number), 'Phone number must match ' + PHONE_NUMBER_EXAMPLE
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to=to_number,
        from_=from_number,
        body=message_body)

if __name__ == '__main__':
    send_sms_message()