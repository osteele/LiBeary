## Project LiBeary ReadMe

Team Members: Celina Bekins, Kaitlyn Keil, Mackenzie Frackleton

Project Vision: The LiBeary is a way for the Olin Library to enable students to find new, interesting books in the library collection. Students only need to ask their local bear via text what it recommends, and a book will be texted back to them. 

Code and contributions: We based this project off of Olin Library's bear-as-a-service with send_sms.py and their Twilio connections and accounts. This is a flask application which communicates with Twilio via ngrok. 

Requirements: Twilio, flask, and pandas.

Setup: 

receive_sms.py now can receive a message using Twilio's REST API & ngrok. The sender receives an SMS response based on the message they send. Also, the inbound is printed to the terminal.

send_sms.py will send a message from the bear; Kaitlyn's script will call it with arguments of our slack bot's phone number and the message to be sent. This will send requests to Slack

Next step is to call Kaitlyn's script.