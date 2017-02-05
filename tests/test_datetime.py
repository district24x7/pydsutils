# -*- coding: utf-8 -*-
"""Unit tests of data util functions
"""
from pdb import set_trace as debug
import unittest
import pytest
import datetime
import pydsutils.datetime as DU


class DateUtilsTest(unittest.TestCase):
    def test_day_diff(self):
        assert DU.day_diff("2017-08-08", "2018-08-07", add_one=True) == 365
        assert DU.day_diff("2017-01-01", "2016-12-31", add_one=False) == -1
        assert DU.day_diff("2017-01-01", "2016-12-31", add_one=True) == 0

        assert DU.day_diff("19800101", "19801231", add_one=True, format="%Y%m%d") == 366  # a leap year

    def test_start_of_week(self):
        """Test start of week
        """
        # Start of week is previous year
        result = DU.start_of_week("2017-01-01", format="%Y-%m-%d")
        self.assertEqual(result, "2016-12-26")

        # Start of week is same year, same month
        result = DU.start_of_week("2017-01-02", format="%Y-%m-%d")
        self.assertEqual(result, "2017-01-02")

        result = DU.start_of_week("20170102", format="%Y%m%d")
        self.assertFalse(result == "2017-01-02")
        self.assertTrue(result == "20170102")

        # Leap year
        result = DU.start_of_week("2016-02-29", format="%Y-%m-%d")
        self.assertEqual(result, "2016-02-29")

        # Input is datetime format
        newdate = datetime.datetime.strptime("2017-01-01", "%Y-%m-%d")
        result = DU.start_of_week(newdate)
        self.assertTrue(result == datetime.datetime.strptime("2016-12-26", "%Y-%m-%d"))
        return

    def test_start_of_month(self):
        """Test start of month
        """
        result = DU.start_of_month("2017-01-01", format="%Y-%m-%d")
        self.assertEqual(result, "2017-01-01")

        result = DU.start_of_month("0999-01-02", format="%Y-%m-%d")
        self.assertTrue(result == "0999-01-01" or result == "999-01-01")

        result = DU.start_of_month("19801202", format="%Y%m%d")
        self.assertFalse(result == "1980-12-01")  # Wrong string format
        self.assertTrue(result == "19801201")

        # Leap year
        result = DU.start_of_month("2016-02-29", format="%Y-%m-%d")
        self.assertEqual(result, "2016-02-01")
        # self.assertRaises(ValueError, DU.start_of_month("2017-02-29"))

        # Input is datetime format
        newdate = datetime.datetime.strptime("1917-12-21", "%Y-%m-%d")
        result = DU.start_of_month(newdate)
        self.assertTrue(result == datetime.datetime.strptime("1917-12-01", "%Y-%m-%d"))
        return

    def test_end_of_month(self):
        """Test end of month
        """
        result = DU.end_of_month("2017-01-01", format="%Y-%m-%d")
        self.assertEqual(result, "2017-01-31")

        result = DU.end_of_month("0999-01-02", format="%Y-%m-%d")
        self.assertTrue(result == "0999-01-31" or result == "999-01-31")

        result = DU.end_of_month("19801202", format="%Y%m%d")
        self.assertFalse(result == "1980-12-31")  # Wrong string format
        self.assertTrue(result == "19801231")

        # Leap year
        result = DU.end_of_month("2016-02-28", format="%Y-%m-%d")
        self.assertEqual(result, "2016-02-29")
        result = DU.end_of_month("1980-02-29", format="%Y-%m-%d")
        self.assertEqual(result, "1980-02-29")
        # self.assertRaises(ValueError, DU.end_of_month("2017-02-29"))

        # Input is datetime format
        newdate = datetime.datetime.strptime("1917-07-21", "%Y-%m-%d")
        result = DU.end_of_month(newdate)
        self.assertTrue(result == datetime.datetime.strptime("1917-07-31", "%Y-%m-%d"))
        return


if __name__ == "__main__":
    unittest.main()
