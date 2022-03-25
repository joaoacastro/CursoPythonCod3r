print(1.1 + 2.2)    # print 3.3000000000000003

from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))  # print 0.1428571428571428571428571429

getcontext().prec = 4
print(Decimal(1) / Decimal(7))  # print 0.1429

print(Decimal.max(Decimal(1), Decimal(7)))     # print 7

# print(dir(Decimal))     # imprimi todas as funções de Decimal

getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))  # print 3.300000000