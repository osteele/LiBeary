## Project LiBeary ReadMe

Team Members: Celina Bekins, Kaitlyn Keil, Mackenzie Frackleton

Project Vision: The LiBeary is a way for the Olin Library to enable students to find new, interesting books in the library collection. Students only need to ask their local bear via text what it recommends, and a book will be texted back to them. 

Code and contributions: We based this project off of Olin Library's bear-as-a-service with send_sms.py and their Twilio connections and accounts. This is a flask application which communicates with Twilio via ngrok. 

Requirements: Twilio, flask, and pandas and a slackbot to post to desired slack account.

Setup: 

Create a bear-secrets.txt file containing the following: 

`# Copy this file to .envrc, and edit your assigned phone number and credentials
# into it.
# Each time you open a new terminal, run `source .envrc`.
# On Windows, run `setx MQTT_URL mqtt://…` etc. instead.
# Pro Tip: Automate this by installing direnv https://direnv.net/.
export MQTT_URL='mqtt://djdnhvdd:PAevqYVXbfbUDzF0Xwe245jOAa37AzlF@termite.rmq.cloudamqp.com:1883/djdnhvdd'
export TWILIO_ACCOUNT_SID='<your account>'
export TWILIO_AUTH_TOKEN='<your authorization token>'
export TWILIO_PHONE_NUMBER='<your twilio phone number in E.164 format>'
export SLACK_PHONE_NUMBER='<your slackbot phone number in E.164 format>'`

If in Linux/macOS, execute `source bear-secrets.txt`. Windows: `setx NAME value` for each export.

Run `pip3 install -r requirements.txt`

`cd scripts` and run `python receive_sms.py`

Running:

Once all requirements are installed, run 'python receive_sms.py'. While this is running, messages sent to the associated Twilio number will go to the bear. If the message contains the word 'recommend', the bear will recommend a book. If the message also contains the word 'nonfiction', the book recommended will be a nonfiction book from the compiled database. If the message does not contain the 'nonfiction' specification, a fiction book will be recommended.

receive_sms.py receives a message using Twilio's REST API & ngrok. The sender receives an SMS response based on the message they send. Also, the inbound is printed to the terminal.

Future:

send_sms.py will send a message from the bear. When a message containing the word 'request' is sent to the bear, the requested book will be forwarded to the library Slack account in order to request the book. A confimation message will also be sent to the original messenger.