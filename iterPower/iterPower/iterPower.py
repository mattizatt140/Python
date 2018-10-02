def iterPow(b, e):
    result = 1
    for i in range(0, e, 1):
        result *= b
    return result

print(iterPow(5, 0))