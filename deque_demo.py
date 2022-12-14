from collections import deque
import itertools

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

print(d.pop())

print(d.popleft())

d.rotate(2)

print(d)

d.rotate(-4)

print(d)

sliced_deque = list(itertools.islice(d, 3, 9))

print(sliced_deque)