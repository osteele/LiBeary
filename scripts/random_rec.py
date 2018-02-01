"""This script will choose a random book from primary_list.csv when the bear is asked
for a recommendation."""

import pandas as pd
import os

def readBooksDatabase(database):
	""" Given a database in CSV format,
	loads it into a pandas dataframe.
	"""
	books = pd.read_csv(database)
	return books


if __name__ == '__main__':
	os.chdir('../docs')
	books = readBooksDatabase('primary_list.csv')
	print(books)