## Celina's Thoughts

receive_sms.py now can receive a message using Twilio's REST API & ngrok. The sender receives an SMS response based on the message they send. Also, the inbound is printed to the terminal.

send_sms.py will send a message from the bear; Kaitlyn's script will call it with arguments of our slack bot's phone number and the message to be sent. This will send requests to Slack

Next step is to call Kaitlyn's script.