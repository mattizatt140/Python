def remainingPay(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        minPayment = balance * monthlyPaymentRate
        balance -= minPayment
        interest = ((annualInterestRate/12.0) * balance)
        balance += interest
    balance = round(balance, 2)
    print("Remaining balance:", balance)

def minimumPay(balance, annualInterestRate):
    minPayment = 0
    copyBalance = balance
    while copyBalance > 0:
        copyBalance = balance
        minPayment += 10
        for i in range(0, 12):
            copyBalance -= minPayment
            interest = ((annualInterestRate/12.0) * copyBalance)
            copyBalance += interest
    balance = round(balance, 2)
    print("Lowest Payment:", minPayment)
   
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance
lowestBalance = 0.01

def minimumPayBi(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    lowerBound = balance / 12
    upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
    originalBalance = balance
    lowestBalance = 0.01

    while abs(balance) > lowestBalance:
   
        balance = originalBalanc
        payment = (upperBound - lowerBound) / 2 + lowerBound

        for month in range(12):
            balance -= payment
            balance *= 1 + monthlyInterestRate

        if balance > 0:
            lowerBound = payment
        else:
            upperBound = payment

    print("Lowest Payment:", round(payment, 2))  
