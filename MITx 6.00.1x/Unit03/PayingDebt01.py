
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthyInterestRate = annualInterestRate/12

for i in range(0, 12):
    minPayment = balance * monthlyPaymentRate
    balance -= minPayment
    interest = balance * monthyInterestRate
    balance = balance + interest
    
    '''print("At the end of month ", i, end=' ')
    print("Payment made is  ", round(minPayment, 2), end=' ')
    print("interest is  ", round(interest, 2), end=' ')
    print("Balance is", round(balance, 2))'''
    

print("Remaining balance:", round(balance,2))
