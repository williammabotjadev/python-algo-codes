from collections import Counter

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
