from collections import deque

d = deque("abracadabra")
print(d)
d.append("z")
print(d)
d.appendleft("a")
print(d)
d.extend("xyz")
print(d)
d.extendleft("abc")
print(d)