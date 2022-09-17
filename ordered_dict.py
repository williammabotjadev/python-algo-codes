# A demo for an Ordered Dict

from collections import OrderedDict

o = OrderedDict({
    'a': 3,
    'b': 2,
    'c': 1
})

print(o)

o_one = OrderedDict()
o_one['one'] = 1
o_one['two'] = 2

o_two = OrderedDict()
o_two['two'] = 2
o_two['one'] = 1

o_three = OrderedDict()
o_three['one'] = 1
o_three['two'] = 2 

print(o_one == o_three)

print(o_two == o_one)