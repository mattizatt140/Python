import random

def stdDev(list):
    mean = sum(list)/float(len(list))
    tot = 0.0
    for e in list:
        tot += (e - mean) ** 2
    std = (tot / len(list)) ** 0.5
    return std

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x * x + y * y) ** 0.5 <= 1.0:
            inCircle += 1
    return 4 * (inCircle / float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates) / len(estimates)
    print('Est. = ' + str(curEst) +\
          ', Std. dev. = ' + str(round(sDev, 6)) \
          + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 2:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

estPi(0.001, 1000)