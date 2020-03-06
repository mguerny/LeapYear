import unittest
from leapyear import LeapYear


class TestFizzBuzz(unittest.TestCase):

    def test_should_return_true_if_divisible_by_400(self):
        self.assertEqual(LeapYear.leapyear(400), True)

    def test_should_return_false_if_divisible_by_100_but_not_by_400(self):
        self.assertEqual(LeapYear.leapyear(356), False)


if __name__ == '__main__':
    unittest.main()

