principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extraPayment = 1000
extraPaymentStart = 60
extraPaymentEnd = 108


while principal > 0:
    if months in range (extraPaymentStart, extraPaymentEnd):
        principal = principal * (1+rate/12) - payment - extraPayment
        total_paid = total_paid + payment + extraPayment
        months += 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        months += 1      

print('Total paid', total_paid, "in", months, "months.")
