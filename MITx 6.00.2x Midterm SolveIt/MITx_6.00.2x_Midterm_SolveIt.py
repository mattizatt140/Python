import logging

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    counterPos = 0
    counterNeg = 0
    while True:
        if test(counterPos):
            return counterPos
        elif test(counterNeg):
            return counterNeg

        counterPos += 1
        counterNeg -= 1
    

#### This test case prints 0 ####
def f(x):
    return x == -183
print(solveit(f))

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))



