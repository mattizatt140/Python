import random
import scipy
import pylab

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # List to hold amount of times 3 similar balls were chosen
    totalTimes = []

    # Run trials
    for i in range(numTrials):

        # Reset contents of balls each trail
        balls = ['r', 'r', 'r', 'g', 'g', 'g']

        # List to hold the balls pulled out
        chosenBalls = []

        # Pull out 3 balls
        for i in range(3):

            ball = random.choice(balls)
            chosenBalls.append(ball)
            balls.remove(ball)

        # Append true if 3 similar balls were chose else append false
        totalTimes.append(True) if chosenBalls.count('r') == 3 or chosenBalls.count('g') == 3 else totalTimes.append(False)

    # Return the ratio of total times 3 similar balls were chosen to total time 3 balls were chosen
    return totalTimes.count(True) / len(totalTimes)

gauss = []
exp = []
rand = []
for i in range(1000):
    gauss.append(random.gauss(50, 10))
    exp.append(random.expovariate(0.5))
    rand.append(random.randint(0, 100))

pylab.hist(gauss)
pylab.hist(exp)
pylab.hist(rand)
pylab.show()
pylab.plot(gauss)
pylab.show()