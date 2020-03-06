class LeapYear:

    @staticmethod
    def leapyear(year):
        answer = False

        if year % 400 == 0:
            answer = True

        if year % 100 == 0 and year % 400 != 0:
            answer = False

        return answer

