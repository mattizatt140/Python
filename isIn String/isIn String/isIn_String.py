def isIn(char, aStr):
    low = 0
    high = len(aStr)
    ans = int(len(aStr) / 2)
    if (len(aStr) == 1 or len(aStr) == 0) and aStr != char:
        return False
    elif aStr[ans] == char:
        return True
    if char < aStr[ans]:
        return isIn(char, aStr[low:ans])
    elif char > aStr[ans]:
        return isIn(char, aStr[ans:len(aStr)])
    
s = "abcd"
print(isIn('e', s))
