# OrderedDict Demo continued

from collections import OrderedDict

d = OrderedDict({
    "one": 1,
    "two": 2
})

print(d)

kvs = [
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6)
]

d.update(kvs)

print(d)