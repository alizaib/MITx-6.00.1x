balance = 3926
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

minPayment = 10
iterations = 0
while minPayment < balance/10:
    if calculateBalance(minPayment) <= 0:
        break
    minPayment += 10
    iterations+=1

print("Iterations", iterations)

print("Lowest Payment: ", minPayment)
