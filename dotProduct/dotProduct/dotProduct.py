def dotProduct(listA, listB):
    listResult = []; result = 0
    for i in range(len(listA)):
        listResult.append(listA[i] * listB[i])
    for i in listResult:
        result += i
    return result

listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA, listB))