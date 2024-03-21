import math


class InvalidBoundaryException(Exception):
    pass


class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        try:
            if start >= end:
                raise InvalidBoundaryException
            else:
                return [x ** 2 for x in range(start, end + 1)]
        except InvalidBoundaryException:
            print("Right bound is less than left")


newList = [math.sqrt(x) for x in SquareGenerator.e_squares(1, 1)]
print(newList)
