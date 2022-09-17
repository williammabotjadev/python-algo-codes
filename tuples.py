# A demo of Tuples

from re import X


tpl = ('a', 'b', 'c')

t = ('a',)

s = tuple("abracadabra")

print(tpl)
print(t)
print(s)

# Tuple unpacking

l = ['one', 'two']

x, y = l

print(x)
print(y)

x, y = y, X

print(x)
print(y)