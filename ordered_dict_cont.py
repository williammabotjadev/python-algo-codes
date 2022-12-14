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

for k, v in d.items():
    print(f"{k} : {v}")

new_od = OrderedDict(sorted(d.items(), key=lambda x: (4 * x[1]) - x[1] ** 2))

print(new_od)

print(new_od.values())