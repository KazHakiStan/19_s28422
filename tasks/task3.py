class SquareGenerator:
    @staticmethod
    def e_squares(start, end):
        return [x ** 2 for x in range(start, end + 1)]


print(SquareGenerator.e_squares(1, 10))
