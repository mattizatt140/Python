animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['e'] = ['elephent']


def how_many(aDict):
    sum = 0
    for k in aDict.keys():
        sum += len(aDict[k])
    return sum

def biggest(aDict):
    start = True
    biggest = 0
    for k in aDict.keys():
        if start:
            biggest = k
            start = False
        else:
            if len(aDict[k]) > len(aDict[biggest]):
                biggest = k
    if type(biggest) == str:
        return biggest
        
emptyList = {}
print(biggest(emptyList))
print(how_many(animals))