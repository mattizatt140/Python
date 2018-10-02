def applyF_filterG(L, f, g):
    filtered = []
    for i in L:
        if g(f(i)):
            filtered.append(i)

    L[:] = filtered
    if L == []:
        return -1
    else:
        return max(L)

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
