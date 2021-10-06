from .__init__ import *


def sumOfAnglesOfPolygonFunc(maxSides=12, format='string'):
    side_count = random.randint(3, maxSides)
    sum = (side_count - 2) * 180

    if format == 'string':
        problem = f"Sum of angles of polygon with {side_count} sides = "
        return problem, sum
    else:
        return side_count, sum


sum_of_polygon_angles = Generator("Sum of Angles of Polygon", 58,
                                  sumOfAnglesOfPolygonFunc, ["maxSides=12"])
