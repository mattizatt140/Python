def uniqueValues(aDict):
    freq = {}
    for i in aDict.values():
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    uniqueKeys = []
    for i in aDict.keys():
        if freq[aDict[i]] == 1:
            uniqueKeys.append(i)
    return uniqueKeys