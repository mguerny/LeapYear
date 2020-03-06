class LeapYear:

    @staticmethod
    def leapyear(year):
        if year % 400 == 0:
            return True
        else:
            return False
