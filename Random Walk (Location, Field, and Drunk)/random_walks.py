def walk(field, drunk, numSteps):
    """
    Moves dnumSteps times; returns the distance between the final 
    location and the location at the start of the walk
    """
    start = field.getLoc(drunk)
    for s in range(numSteps):
        field.moveDrunk(drunk)
    return start.distFrom(field.getLoc(drunk))

def simWalks(numSteps, numTrials, dClass):
    """
    Assumes numSteps an int >= 0, numTrials an
    int > 0, dClass a subclass of Drunk
    """

    # Simulates numTrials walks of numSteps steps each
    # Returns a list of final distances for each trial
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numTrials), 1))

    return distances

