# A Demo of Set Operations

s_one = {'ab', 3, 4, (5, 6)}
s_two = {'ab', 7, (7, 6)}

print(s_one.difference(s_two))

print(s_one.intersection(s_two))

print(s_one.union(s_two))