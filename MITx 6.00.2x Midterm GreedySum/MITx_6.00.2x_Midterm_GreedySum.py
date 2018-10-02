def calcList(L, LoM):
    sum = 0
    for i in range(len(L)):
        try:
            sum += L[i] * LoM[i]
        except IndexError:
            break
    return sum

def calcSum(L):
    sum = 0
    for i in L:
        sum += i
    return sum

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    # Create a list to hold multipliers
    LoM = []

    # Create loop to cycle through each element of L
    for i in L:

        # Create loop to test multipliers for element of L
        for j in range(s, -1, -1):
            multiplier = j

            # Create temp multiplier list
            tempLoM = LoM.copy(); tempLoM.append(j)

            # Test equation to make sure multiplier qualifies
            if calcList(L, tempLoM) < s:
                LoM.append(j)
                break

            elif calcList(L, tempLoM) == s:
                LoM.append(j)

                # Return sum of List of Multipliers if solution found
                return sum(LoM)

    # Return if no solution found
    return "no solution"

