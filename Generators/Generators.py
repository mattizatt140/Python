def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

def prime():
    yield 2
    pri = 3; LoP = [2]
    for i in range(pri, 1000000000000000):
        for j in LoP:
            if i % j == 0:
                break
            else:
                if j == LoP[-1]:
                    LoP.append(i)
                    yield i

pri = genFib()
for i in pri:
    print(i)