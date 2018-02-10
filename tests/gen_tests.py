import os
import sys
import pytest

from unittest.mock import MagicMock, patch  # noqa: I001

# noqa: I003
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.libeary import *

def test_recommend():
	""" Tests the Recommender class """
	rec = Recommender("docs/primary_list.csv")
	t1 = rec.chooseWhich("recommend fiction")
	assert (isinstance(t1[0], str) and isinstance(t1[1], str) and t1[2]!=1)
	t2 = rec.chooseWhich("recommend nonfiction")
	assert (isinstance(t2[0], str) and isinstance(t2[1], str) and t2[2]!=0)
	t3 = rec.chooseWhich("recommend")
	assert (isinstance(t3[0], str) and isinstance(t3[1], str) and t3[2]!=1)

def test_wrapper():
	""" Tests the LiBeary wrapper class for general proper formatting """
	libear = LiBeary("docs/primary_list.csv");
	t1 = libear.makeRecommendation("recommend fiction")
	assert (isinstance(t1, str) and " by " in t1)
	t2 = libear.makeRecommendation("recommend nonfiction")
	assert (isinstance(t2, str) and " by " in t2)
	t3 = libear.makeRecommendation("recommend")
	assert (isinstance(t3, str) and " by " in t3)

# if __name__ == '__main__':
# 	test_recommend()
# 	test_wrapper()