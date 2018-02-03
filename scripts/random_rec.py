"""This script will choose a random book from primary_list.csv when the bear is asked
for a recommendation."""

import pandas as pd
import os

def readBooksDatabase(database):
	""" Given a database in CSV format,
	loads it into a pandas dataframe.
	Returns two pandas dataframes: one for fiction,
	one for nonfiction
	"""
	books = pd.read_csv(database)
	fiction = books[books['Nonfiction'] == 0]
	nonfiction = books[books['Nonfiction'] == 1]
	return fiction, nonfiction

def generateRandom(df):
	""" Given a dataframe, returns the name
	and title of the book. """
	rec = df.sample()
	for _,row in rec.iterrows(): # A hack to return the first row title and author. It works since we only want one rec
		return row.Title, row.Author

if __name__ == '__main__':
	os.chdir('../docs')
	fiction, nonfiction = readBooksDatabase('primary_list.csv')
	fic_title, fic_author = generateRandom(fiction)
	nfic_title, nfic_author = generateRandom(nonfiction)
	print("Fiction Recommendation:\n",fic_title, "by", fic_author)
	print("Nonfiction Recommendation:\n", nfic_title, "by", nfic_author)