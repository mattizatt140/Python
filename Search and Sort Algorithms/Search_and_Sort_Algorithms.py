import time
import random

def bisect_search1(L, e): #Divide and conquor search method
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e) #search top half of list
        else:
            return bisect_search1(L[half:], e) #search bottom half of list

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    return bisect_search_helper(L, e, 0, len(L) - 1)

def bogo_sort(L):
    while L != sorted(L):
        random.shuffle(L)

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def selective_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    #Merges sorted data
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while (i < len(left)):
            result.append(left[i])
            i += 1
        while (j < len(right)):
            result.append(right[j])
            j += 1
        return result
    #Code block below seperates data
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle]) 
        right = merge_sort(L[middle:])
        return merge(left, right)

if __name__ == '__main__':
    L = []
    for i in range(3):
        num = random.randint(0, 10000)
        L.append(num)

    start = time.clock()
    L = merge_sort(L)
    end = time.clock()
    print(str(end - start) + 's')
    