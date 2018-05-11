
import unittest
from hackerrank.HostCrowding import *


class MyTest(unittest.TestCase):

    def test_cases(self):
        resultsPerPage = 5
        results = [
            "1,28,300.6,San Francisco",
            "4,5,209.1,San Francisco",
            "20,7,203.4,Oakland",
            "6,8,202.9,San Francisco",
            "6,10,199.8,San Francisco",
            "1,16,190.5,San Francisco",
            "6,29,185.3,San Francisco",
            "7,20,180.0,Oakland",
            "6,21,162.2,San Francisco",
            "2,18,161.7,San Jose",
            "2,30,149.8,San Jose",
            "3,76,146.7,San Francisco",
            "2,14,141.8,San Jose"]

        output = [
            "1,28,300.6,San Francisco",
            "4,5,209.1,San Francisco",
            "20,7,203.4,Oakland",
            "6,8,202.9,San Francisco",
            "7,20,180.0,Oakland",
            "",  # this is a page separator
            "6,10,199.8,San Francisco",
            "1,16,190.5,San Francisco",
            "2,18,161.7,San Jose",
            "3,76,146.7,San Francisco",
            "6,29,185.3,San Francisco",
            "",  # this is a page separator
            "6,21,162.2,San Francisco",
            "2,30,149.8,San Jose",
            "2,14,141.8,San Jose"]

        my_output = paginate(resultsPerPage, results)
        print(my_output)
