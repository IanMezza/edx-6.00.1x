"""Problem 1 - Paying Debt off in a Year
Write a program to calculate the credit card balance after one year if a person only
pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy.
"""
def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    monthlyUnpaidBalance = 0
    interest = 0
    for i in range(13):
        if i > 0:
            balance = monthlyUnpaidBalance + interest
            pass
        minPayment = balance * monthlyPaymentRate
        monthlyUnpaidBalance = balance - minPayment
        interest = annualInterestRate/12 * monthlyUnpaidBalance
    print('Remaining balance: ', round(balance, 2))
    return round(balance, 2)