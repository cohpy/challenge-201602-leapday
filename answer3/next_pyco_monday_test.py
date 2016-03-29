import unittest
from next_pyco_monday import *

class TestNextMeetupOnLeapYear(unittest.TestCase):

	def test_is_leap_year_4_year_cases(self):
		self.assertTrue(is_leap_year(4))
		self.assertTrue(is_leap_year(444))
		self.assertTrue(is_leap_year(2016))

	def test_is_not_leap_year_100_year_cases(self):
		self.assertFalse(is_leap_year(100))
		self.assertFalse(is_leap_year(200))
		self.assertFalse(is_leap_year(2100))

	def test_is_leap_year_400_year_cases(self):
		self.assertTrue(is_leap_year(400))
		self.assertTrue(is_leap_year(800))
		self.assertTrue(is_leap_year(2000))

	def test_is_not_leap_year_non_4_year_cases(self):
		self.assertFalse(is_leap_year(101))
		self.assertFalse(is_leap_year(203))
		self.assertFalse(is_leap_year(2017))

	def test_next_leap_year_4_year_case(self):
		self.assertEqual(next_leap_year(2017), 2020)

	def test_next_leap_year_100_year_case(self):
		self.assertEqual(next_leap_year(2099), 2104)

	def test_next_leap_year_400_year_case(self):
		self.assertEqual(next_leap_year(1999), 2000)

	def test_feb_29_is_monday_2016_case_true(self):
		self.assertTrue(feb_29_is_monday(2016))

	def test_feb_29_is_monday_2012_case_false(self):
		self.assertFalse(feb_29_is_monday(2012))

	def test_feb_29_is_monday_throws_error_on_non_leapyear(self):
		with self.assertRaises(ValueError):
		    feb_29_is_monday(2011)

	def test_next_pyco_leapyear_monday_2015_case(self):
		self.assertEqual(next_pyco_leapyear_monday(2015), 2016)


if __name__ == '__main__':
		unittest.main()
