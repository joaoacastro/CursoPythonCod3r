a = '123'
b = ' de Oliveira 4'
print(a+b) # print 123 de Oliveira 4

print(a.__add__(b)) # print 123 de Oliveira 4
print(str.__add__(a, b)) # print 123 de Oliveira 4

print(len(a)) # print 3
print(a.__len__()) # print 3
print('1' in a) # print True
print(a.__contains__('1')) # print True
