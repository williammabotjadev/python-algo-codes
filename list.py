s = "able was i ere i saw elba"
col = list(s)

col.append(' - Napoleon')

print(" ".join(col))

l = []

l.extend(s)

print(l)

print(col.count('a'))

print(col.index('a'))

print(col.index('a', 4, len(col)))
