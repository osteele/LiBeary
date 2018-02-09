""" Contains the LiBeary Class. """
import pandas as pd

class LiBeary():
	""" Contains a recommender to give random
	recommendations to the texter. Currently
	just a wrapper, but built to be easy to 
	expand in the future.
	"""

	def __init__(self):
		self.reccer = Recommender("primary_list.csv")

	def makeRecommendation(self, message):
		""" Given a text, gets a recommendation
		from the Recommender and says it through
		the bear. 
		"""
		title, author, _ = self.reccer.chooseWhich(message)
		bear_statement = title + " by " + author
		return bear_statement

class Recommender():
	""" A class that contains the databases and
	a number of methods to support recommending
	books. """
	def __init__(self, database):
		""" Given a database, constructs a fiction
		and nonfiction pandas DataFrame """
		self.fic, self.nfic = self.readBooksDatabase(database)

	def readBooksDatabase(self, database):
		""" Given a database in CSV format,
		loads it into a pandas dataframe.
		Returns two pandas dataframes: one for fiction,
		one for nonfiction
		"""
		books = pd.read_csv(database)
		fiction = books[books['Nonfiction'] == 0]
		nonfiction = books[books['Nonfiction'] == 1]
		return fiction, nonfiction

	def chooseWhich(self, userString):
		""" Taken the input of a text, finds
		whether it requested fiction or nonfiction
		and returns the recommendation from the proper
		database """
		if "nonfiction" in userString.lower():
			return self.generateRandom(self.nfic)
		else:
			return self.generateRandom(self.fic)

	def generateRandom(self, df):
		""" Given a dataframe, returns the name
		and title of the book. """
		rec = df.sample()
		for _,row in rec.iterrows(): # A hack to return the first row title and author. It works since we only want one rec
			return row.Title, row.Author, row.Nonfiction

if __name__ == '__main__':
	libeary = LiBeary()