import os
low = 0
high = 100
ans = int(((high + low)/ 2))

print("Think of a number between 0 and 100")

while True:
    print("Is your secret number", ans ,"?")
    userInput = input("h, l, c: ")
    
    if userInput == 'l':
        low = ans
        ans = int(((high + low) / 2))
    elif userInput == 'h':
        high = ans
        ans = int(((high + low) / 2))
    elif userInput == 'c':
        break;
    else:
        pass
        
    os.system("cls")
print("Game over: Your secret number was", ans)
