"""This script will choose a random book from primary_list.csv when the bear is asked
for a recommendation."""

import pandas as pd
import os

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
			return row.Title, row.Author

	def tester(self):
		t1 = reccer.chooseWhich("Fiction plz!")
		if not (t1[0] != "Error"): raise AssertionError("Test 1 failed")
		t2 = reccer.chooseWhich("Gimme a nonfiction!")
		if not (t2[0] != "Error"): raise AssertionError("Test 2 failed")
		t3 = reccer.chooseWhich("I want a potato")
		if not (t3[0] == "Error"): raise AssertionError("Test 3 failed")
		t4 = reccer.chooseWhich("FICTION")
		if not (t4[0] != "Error"): raise AssertionError("Test 4 failed")
		t5 = reccer.chooseWhich("fic")
		if not (t5[0] == "Error"): raise AssertionError("Test 5 failed")
		t6 = reccer.chooseWhich("n onfiction") # currently, this will give a fiction rec
		if not (t6[0] != "Error"): raise AssertionError("Test 6 failed")

if __name__ == '__main__':
	os.chdir('../docs')
	reccer = Recommender('primary_list.csv')
	reccer.tester()
	# fic_title, fic_author = reccer.chooseWhich("Fiction plz!")
	# nfic_title, nfic_author = reccer.chooseWhich("Gimme a nonfiction!")
	# er_t, er_a = reccer.chooseWhich("I want a potato")
	# print("Fiction Request:\n\t",fic_title, "by", fic_author)
	# print("Nonfiction Request:\n\t", nfic_title, "by", nfic_author)
	# print("Erroneous Request:\n\t", er_t, "by", er_a)