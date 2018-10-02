def compare(x, y, func):
    return func(x, y)

print(compare(4, 3, func = lambda x, y: True if(x>y) else False))