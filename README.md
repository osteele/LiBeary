## Celina's Thoughts

receive_sms.py now can receive a message using Twilio's REST API & ngrok. The sender receives an SMS response that reads "Ahoy! Thanks so much for your message."

send_sms.py will send a message from the bear; Kaitlyn's script will call it with arguments of our slack bot's phone number and the message to be sent. This will send requests to Slack

Next step is to make receive_sms.py pull out the message body and call Kaitlyn's script on it