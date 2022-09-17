# A Demo of Set Operations

from asyncio import set_child_watcher


s_one = {'ab', 3, 4, (5, 6)}
s_two = {'ab', 7, (7, 6)}

print(s_one.difference(s_two))

print(s_one.intersection(s_two))

print(s_one.union(s_two))

print('ab' in s_one)

print('ab' not in s_one)

for i in s_one:
    print(i)

s_one.add(frozenset(s_two))

print(s_one)

f_one = frozenset(s_one)
f_two = frozenset(s_two)

set_dict = {
    f_one: "frozen set one",
    f_two: "frozen set two"
}

print(set_dict)