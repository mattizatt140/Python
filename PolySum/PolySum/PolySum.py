from math import tan
from math import pi

def polysum(n, s):
    area = (0.25 * n * (s * s)) / (tan(pi/n))
    perimeter = n * s
    result = format(area + (perimeter ** 2))
    return round(result, 4)

