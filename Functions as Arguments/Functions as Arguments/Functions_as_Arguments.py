def addFive(a):
    return a + 5

def listAddFive(myList, addFive):
    for i in range(len(myList)):
        myList[i] = addFive(myList[i])

def f(x):
    return abs(x/5)

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

