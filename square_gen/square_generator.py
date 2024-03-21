# from square_gen import exception
from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @staticmethod
    @abstractmethod
    def e_squares(start, end):
        pass
        # try:
        #     if start >= end:
        #         raise exception.InvalidBoundaryException
        #     else:
        #         return [x ** 2 for x in range(start, end + 1)]
        # except exception.InvalidBoundaryException:
        #     print("Right bound is less than left")
