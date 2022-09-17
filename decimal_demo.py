import decimal 

x = decimal.Decimal(3.14)
y = decimal.Decimal(2.74)

print(x * y)

decimal.getcontext().prec = 4 

print(x * y)