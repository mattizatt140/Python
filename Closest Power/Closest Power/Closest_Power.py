def closest_power(base, num):
    closestPow = 0; closestResult = 1
    for exp in range(100):
        result = base**exp
        if abs(result - num) < abs(closestResult - num):
            closestResult = result
            closestPow = exp
    return closestPow