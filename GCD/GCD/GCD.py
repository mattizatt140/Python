def smaller(a, b):
    return a < b

def gcditr(a, b):
    if smaller(a, b):
        i = a
    else:
        i = b

    for i in range(i, 0, -1):
        if i == 1: break
        elif (a % i == 0) and (b % i == 0):
            return i
    return "No GCD"

def gcdRec(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRec(b, a % b)
