class LeapYear:

    @staticmethod
    def leapyear(year):
        return year % 400 == 0 or not (year % 100 == 0 and year % 400 != 0)
