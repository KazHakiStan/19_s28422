from square_gen import square_generator
from square_gen import exception


class CubicGenerator(square_generator.SquareGenerator):
    @staticmethod
    def e_cubes(start, end):
        try:
            if start >= end:
                raise exception.InvalidBoundaryException
            else:
                return [x ** 3 for x in range(start, end + 1)]
        except exception.InvalidBoundaryException:
            print("Right bound is less than left")
