class LeapYear:

    # leap years example : 1600, 2000, 2400, 2004, 2008
    # NOT leap years example : 1700, 1800, 2017, 2018

    @staticmethod
    def leapyear(year):

        if (year % 100 == 0 and year % 400 != 0) or year % 4 != 0:
            return False

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True

        return False
