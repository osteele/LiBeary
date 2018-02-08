## Project LiBeary ReadMe

**Team Members**: Celina Bekins, Kaitlyn Keil, Mackenzie Frackleton

*Project Vision*: The LiBeary is a way for the Olin Library to enable students to find new, interesting books in the library collection. Students only need to ask their local bear via text what it recommends, and a book will be texted back to them. Students may also request books by texting their request and the book title, which will message the Olin Library slack account.

*Code and contributions*: We based this project off of Olin Library's bear-as-a-service with send_sms.py and their Twilio connections and accounts. This is a flask application which communicates with Twilio via ngrok. 

*Requirements*: Twilio, flask, and pandas and a slackbot to post to desired slack account.

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

`cd scripts` and run `python receive_sms.py`

Inside `docs/`, create a csv file called `primary_list.csv` which contains a column called "Author", "Title", and "Nonfiction". "Nonfiction" should contain 1 if the book is nonfiction and a 0 otherwise. Populate this with desired titles. This is your book database.

### Running

Once all requirements are installed, run 'python receive_sms.py'. While this is running, messages sent to the associated Twilio number will go to the bear. If the message contains the word 'recommend', the bear will recommend a book. If the message also contains the word 'nonfiction', the book recommended will be a nonfiction book from the compiled database. If the message does not contain the 'nonfiction' specification, a fiction book will be recommended.

For example, 'recommend nonfiction' will respond with a nonfiction book, whereas 'recommend me a good book!' will figve a fiction title.

Requests are made by sending a message in the format of 'request <book title>'. This will then forward the book title (and anything in the message besides 'request') to the slackbot to be posted. A confirmation will be sent to the original messenger.
