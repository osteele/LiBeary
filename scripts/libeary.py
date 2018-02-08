""" Contains the LiBeary Class. """

from random_rec import Recommender

class LiBeary():
	""" Contains a recommender to give random
	recommendations to the texter. Also will
	message the library's book request slack
	when a request for a new book is sent. """

	def __init__(self):
		self.reccer = Recommender("../docs/primary_list.csv")
		self.running = True

	def newMessage(self, message):
		""" Given a message, determines whether the
		texter desires a recommendation or to make
		a book request. Calls the appropriate method.

		input - String containing the text message body
		"""
		# OUTDATED
		message = message.strip()
		if message[:8].lower() == "request:":
			return self.submitRequest(message[8:].strip())
		else:
			return self.makeRecommendation(message)

	def submitRequest(self, message, num_to_send_to):
		""" Given a text, messages the text to the
		library slack and says 'Request Submitted'
		"""
		# TODO: figure out the interface here
		# send_slack_message(message)
		# bear_talk("Request Submitted")
		return "Request Submitted"

	def makeRecommendation(self, message):
		""" Given a text, gets a recommendation
		from the Recommender and says it through
		the bear. 
		"""
		title, author, _ = self.reccer.chooseWhich(message)
		bear_statement = title + " by " + author
		return bear_statement

	def run(self):
		""" Loops until we quit. Mostly testing. """
		# NOT USED
		while self.running:
			message = input("This is DEFINITELY a text message: ")
			if message in ['x', 'exit', 'quit']: break
			self.newMessage(message)

if __name__ == '__main__':
	libeary = LiBeary()
	libeary.run()