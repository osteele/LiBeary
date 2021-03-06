## Project LiBeary ReadMe

**Team Members**: Celina Bekins, Kaitlyn Keil, Mackenzie Frackleton

*Project Vision*: The LiBeary helps the Olin Library enable students to find new, interesting books in the library collection. Students only need to ask their local bear via text what it recommends, and a book title will be texted back to them. Students may also request books by texting the bear, which will message the Olin Library Slack account.

*Code and contributions*: We based this project off of Olin Library's bear-as-a-service with send_sms.py and their Twilio connections and accounts. This is a Flask application which communicates with Twilio via ngrok.

*Requirements*: Twilio (install), a Twilio account/phone number, Flask, and pandas, as well as a slackbot to post to the desired Slack account.

### Setup

Create a bear-secrets.txt file containing the following:

~~~~
export MQTT_URL='mqtt://djdnhvdd:PAevqYVXbfbUDzF0Xwe245jOAa37AzlF@termite.rmq.cloudamqp.com:1883/djdnhvdd'

export TWILIO_ACCOUNT_SID='<your account>'

export TWILIO_AUTH_TOKEN='<your authorization token>'

export TWILIO_PHONE_NUMBER='<your twilio phone number in E.164 format>'

export SLACK_PHONE_NUMBER='<your slackbot phone number in E.164 format>'`
~~~~

If in Linux/macOS, execute `source bear-secrets.txt`. Windows: `setx NAME value` for each export.

Run `pip3 install -r requirements.txt`

Inside `data/`, create a csv file called `primary_list.csv` which contains a column called "Author", "Title", and "Nonfiction". "Nonfiction" should contain 1 if the book is nonfiction and a 0 otherwise. Populate this with desired titles. This is your book database.

`cd scripts` and run `python receive_sms.py`

Open a new terminal and run `./ngrok http 5000`

Copy the forwarding URL. Go to your Twilio dashboard, then go to configure your phone number. Under "Messaging," make sure that "Configure with" is set to Webhooks/TwiML Bins, then paste your URL in the "A Message Comes In" field with the format `{your URL}/sms`.

### Running

Keep the two terminals running `receive_sms.py` and `ngrok` open. While these are running, messages sent to the associated Twilio number will go to the bear. If the message contains the word 'recommend', the bear will recommend a book. If the message also contains the word 'nonfiction', the book recommended will be a nonfiction book from the compiled database. If the message does not contain the 'nonfiction' specification or if it contains a 'fiction' specification, a fiction book will be recommended.

For example, 'recommend nonfiction' will respond with a nonfiction book, whereas 'recommend me a good book!' will give a fiction title.

Requests are made by sending a message in the format of 'request <book title>'. This will then forward the book title (and anything in the message besides 'request') to the slackbot to be posted. A confirmation will be sent to the original messenger.

Messages that do not fit this format will receive a response message that asks, 'Sorry, say that again?'

### What Next

Next steps include working on a database connection (which should include formal system of storing books); expanding the recommend database to the new acquisitions collection; including a second db for book request so that only the first request posts to slack and the number of requests is stored in the database. An optional reach would add voice support.
