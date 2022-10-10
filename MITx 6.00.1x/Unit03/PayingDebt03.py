balance = 320000
annualInterestRate = 0.2

def calculateBalance(minPayment):
    _balance = balance
    monthyInterestRate = annualInterestRate/12

    for i in range(0, 12):
        
        _balance -= minPayment
        interest = _balance * monthyInterestRate
        _balance = _balance + interest
    
        '''print("At the end of month ", i, end=' ')
        print("Payment made is  ", round(minPayment, 2), end=' ')
        print("interest is  ", round(interest, 2), end=' ')
        print("Balance is", round(balance, 2))'''

    return round(_balance,2)

monthlyInterestRate = annualInterestRate/12
lowerbound = balance/12
upperbound = (balance * (1 + monthlyInterestRate)**12)/12
minPayment = (lowerbound + upperbound)/2

iterations = 0
while lowerbound < balance/10:
    iterations += 1    
    remainingBalance = calculateBalance(minPayment)

    if remainingBalance == 0:
        break
    elif remainingBalance < 0:
        upperbound = minPayment
    else:
        lowerbound = minPayment
    
    minPayment = (lowerbound + upperbound)/2
    

print("Iterations", iterations)
print("Lowest Payment: ", round(minPayment, 2))

