import math
x = float(input("Input: "))
epsilon = 0.01
numGuesses = 0
if x < 1.0:
    low = x
    high = 1
else:
    low = 1
    high = x

ans = (high + low/2.0)

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
    print('numGuesses = ' + str(numGuesses))
    print(str(ans) + ' is close to square root of ' + str(x))
    print()
       
print("Number of Guesses:", numGuesses)
print("Sqrt:", ans)
