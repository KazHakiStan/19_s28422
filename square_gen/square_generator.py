import exception


class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        try:
            if start >= end:
                raise exception.InvalidBoundaryException
            else:
                return [x ** 2 for x in range(start, end + 1)]
        except exception.InvalidBoundaryException:
            print("Right bound is less than left")
        pass
