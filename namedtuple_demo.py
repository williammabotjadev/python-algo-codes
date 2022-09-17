# A demo for the NamedTuple 

from collections import namedtuple

area = namedtuple('area', 'x y z')

a_one = area(x=0.5, y=1, z=3.5)

print(a_one.x * a_one.y * a_one.z)


