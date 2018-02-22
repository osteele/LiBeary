import os
import pandas as pd

# Use a variable, so that this file and gen_tests.py stay in sync.
# (However, see the comment in gen_tests.py).
#
# Optional: this uses os.path.join and __file__ to look for the file relative
# to the source file instead of the current working directory. This allows this
# script to run no matter where it's run from. If the terminal is in the scripts
# directory, `python3 libeary.py` still works, but if from the project root,
# `python scripts/libeary.py` now works.
primary_list_path = os.path.join(os.path.dirname(__file__), '../data/primary_list.csv')


class LiBeary():
	""" Contains a recommender to give random
	recommendations to the texter. Currently
	just a wrapper, but built to be easy to
	expand in the future.
	"""

	def __init__(self, db_file=primary_list_path):
		self.reccer = Recommender(db_file)

	def makeRecommendation(self, message):
		""" Given a text, gets a recommendation
		from the Recommender and says it through
		the bear.
		"""
		title, author, _ = self.reccer.chooseWhich(message)
		bear_statement = title + " by " + author
		# Alternatives to the preceding line:
		# 	bear_statement = "{} by {}".format(title, author)
		# 	bear_statement = "{title} by {author}".format(title=title, author=author)
		#	bear_statement = f"{title} by {author}"
		#
		# In this case they're nearly equal. (Actually, the original is a little
		# less verbose.) The alternatives are nice when the formatting is more
		# complex. The second aternative, in particular, is useful when the
		# formats are from a data structure such as a list or dictionary, or
		# from a data file, so that the wording can be easily edited
		# independently of the source code, for example by a person with a
		# different skill set.
		return bear_statement


class Recommender():
	"""A class that contains the databases and
	a number of methods to support recommending
	books. """

	def __init__(self, database):
		""" Given a database, constructs a fiction
		and nonfiction pandas DataFrame
		"""
		self.fic, self.nfic = self.readBooksDatabase(database)

	def readBooksDatabase(self, database):
		""" Given a database in CSV format,
		loads it into a pandas dataframe.
		Returns two pandas dataframes: one for fiction,
		one for nonfiction
		"""
		# Since you use it more than once, consider using a global variable
		# (really, a constant – but Python uses variables for these too) for
		# 'Nonfiction', to reduce the risk that you'll mis-type it somewhere.
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
		_, row = next(rec.iterrows())
		return row.Title, row.Author, row.Nonfiction

if __name__ == '__main__':
	libeary = LiBeary()
