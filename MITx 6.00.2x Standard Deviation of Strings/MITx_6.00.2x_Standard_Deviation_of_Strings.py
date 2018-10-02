import math
import numpy

def listMean(L):
    # Calculate mean length
    mean = 0
    for string in L:
        mean += len(string)
    try:
        mean /= len(L)
    except ZeroDivisionError:
        return float('NaN')
    return mean

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    # Calculate mean length
    if len(L) == 0:
        return float('NaN')

    mean = listMean(L)
    
    # Calculate standard deviation
    sumOfLen = 0
    for string in L:
        sumOfLen += (len(string) - mean) ** 2

    stdDev = (sumOfLen / len(L)) ** 0.5
    return stdDev
    
L = ['apples', 'oranges', 'kiwis', 'pineapples']
stdDev = stdDevOfLengths([10, 4, 12, 15, 20, 5])