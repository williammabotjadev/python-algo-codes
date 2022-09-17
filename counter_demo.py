from collections import Counter
from curses import init_color
from mimetypes import init

c = Counter("abracadabra")

print(c)

c_one = Counter({
    'a': 1,
    'b': 2,
    'c': 4
})

print(c_one)

c_two = Counter(
    x=2,
    y=4,
    z=6
)

print(c_two)

init_count = Counter()

print(init_count)

init_count.update('abba')

print(init_count)

init_count.update({
    'a': 2
})

print(init_count)

for i in init_count:
    print(f"{i} : {init_count[i]}")

print(c.most_common())

init_count.subtract('a')

print(init_count)