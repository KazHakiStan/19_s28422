import math
import square_generator

newList = [math.sqrt(x) for x in square_generator.SquareGenerator.e_squares(1, 1)]
print(newList)
