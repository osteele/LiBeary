# `pytest` and `pytest-watch` didn't actually run this file. For Pytest's test
# discovery to work, the filename needs to end in `_test.py`, not `_tests.py`.
# Pytest is very picky.
import os
import numpy
import sys
import pytest

from unittest.mock import MagicMock, patch  # noqa: I001

# noqa: I003
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))
# `from scripts.libeary` doesn't work, because `scripts` is not a Python
# package. (A Python package can contain multiple modules, or packages that
# themselves contain modules. This is what permits the `scripts.libeary` syntax
# to import a module within a package, which on disk is a file within a
# directory.) It could be turned into a package by adding a
# `scripts/__init__.py` file (which can be empty). Instead, I've modified the
# line above to add the scripts directory itself to the Python path, which makes
# individual files in that in directory visible to `import` as modules.
from libeary import *


def test_recommend():
	# I wouldn't bother with function comments for test functions. The purpose
	# should be evident from the name of the test.

	# This function and the next function use the data file that the user has
	# been asked to replace. This is fragile: if the user updates the production
	# data, the test can fail. (In this case it isn't much of a risk, since the
	# test depends on so little about the data — just that there's a fiction
	# and a non-fiction row. But in general it's an issue, and it would be if
	# the tests did more, for example test a particular format.)
	rec = Recommender(primary_list_path)
	t1 = rec.chooseWhich("recommend fiction")
	assert isinstance(t1[0], str) and isinstance(t1[1], str) and t1[2] != 1
	t2 = rec.chooseWhich("recommend nonfiction")
	assert isinstance(t2[0], str) and isinstance(t2[1], str) and t2[2] != 0
	t3 = rec.chooseWhich("recommend")
	assert isinstance(t3[0], str) and isinstance(t3[1], str) and t3[2] != 1


# Here's an alternate implementation of test_recommend, that tests for the exact
# data that's returned. In order for this to work, functions that use random-
# ness need to return the same value each time. This is done by "seeding" the
# (pseudo-)random sequence to the same value each time. For most functions
# in Python, this is done by importing the random module and calling
# `random.seed(1)`. Numpy (which Pandas uses) contains its own pseudo-random
# number generator, so instead of importing random, we import numpy (to get
# numpy.random), and instead of calling `random.seed(1)`, we call
# `numpy.random.seed(1)`. [Any other number than 1 would work too. It's just
# important that it be the same each time this test function is run, so that
# the functions that it calls will return the same value each time.]
#
# This definition replaces the previous definition, that has the same name. You
# wouldn't normally include both in the same file. I'm doing it to illustrate
# both approaches.
def test_recommend():
	# This more specific test *does* require that the CSV file remain stable (else
	# you need to update all the tests).
	#
	# FIXME Use a separate data file just for testing.
	rec = Recommender(primary_list_path)
	numpy.random.seed(1)
	t1 = rec.chooseWhich("recommend fiction")
	# FIXME it looks like a bug that the sometimes starts with a space
	# I've removed the `assert instance…`. Testing the actual data is more
	# specific than testing the types.
	assert t1 == ('Americanah', ' Chimamanda Ngozi Adichie', 0)
	t2 = rec.chooseWhich("recommend nonfiction")
	assert t2 == ('Spacelab', 'Douglas R. Lord', 1)
	t3 = rec.chooseWhich("recommend")
	assert t3 == ('The Color Purple', ' Alice Walker', 0)


def test_wrapper():
	# TODO the same treatment that's applied to the second implementation of
	# test_recommend, above, can be used here.
	libear = LiBeary(primary_list_path)
	t1 = libear.makeRecommendation("recommend fiction")
	assert isinstance(t1, str) and " by " in t1
	t2 = libear.makeRecommendation("recommend nonfiction")
	assert isinstance(t2, str) and " by " in t2
	t3 = libear.makeRecommendation("recommend")
	assert isinstance(t3, str) and " by " in t3
