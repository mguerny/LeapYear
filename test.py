import unittest
from leapyear import LeapYear


class TestFizzBuzz(unittest.TestCase):

    def test_should_return_true_if_divisible_by_400(self):
        self.assertEqual(LeapYear.leapyear(400), True)

    def test_should_return_false_if_divisible_by_100_but_not_by_400(self):
        self.assertEqual(LeapYear.leapyear(500), False)

    def test_should_return_true_if_divisible_by_4_but_not_by_100(self):
        self.assertEqual(LeapYear.leapyear(104), True)


if __name__ == '__main__':
    unittest.main()

